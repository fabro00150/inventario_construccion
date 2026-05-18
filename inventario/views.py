from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Material, Orden, Existencia, Categoria, Producto, Venta, DetalleVenta, Configuracion, Seccion
from .forms import MaterialForm, OrdenForm, CategoriaForm, ProductoForm, VentaForm, ConfiguracionForm, SeccionForm
from django.db.models import Sum

@login_required
def dashboard(request):
    total_ventas = Venta.objects.count()
    ingresos_totales = Venta.objects.aggregate(Sum('total'))['total__sum'] or 0
    productos_mas_vendidos = DetalleVenta.objects.values('producto__nombre').annotate(total_vendido=Sum('cantidad')).order_by('-total_vendido')[:5]
    alerta_materiales = Material.objects.filter(existencia__cantidad_disponible__lt=5)
    alerta_productos = Producto.objects.filter(stock__lt=5)
    context = {
        'total_ventas': total_ventas,
        'ingresos_totales': ingresos_totales,
        'productos_mas_vendidos': productos_mas_vendidos,
        'alerta_materiales': alerta_materiales,
        'alerta_productos': alerta_productos,
    }
    return render(request, 'inventario/dashboard.html', context)

def catalogo(request):
    secciones = Seccion.objects.prefetch_related('productos').all()
    return render(request, 'inventario/catalogo.html', {'secciones': secciones})

# Views para Material
@login_required
def lista_materiales(request):
    materiales = Material.objects.all()
    return render(request, 'inventario/materiales/material_lista.html', {'materiales': materiales})

@login_required
def formulario_material(request, id=None):
    if id:
        material = get_object_or_404(Material, id=id)
    else:
        material = None
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect('lista_materiales')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'inventario/materiales/material_formulario.html', {'form': form})

@login_required
def eliminar_material(request, id):
    material = get_object_or_404(Material, id=id)
    if request.method == 'POST':
        material.delete()
    return redirect('lista_materiales')

# Views para Seccion
@login_required
def lista_secciones(request):
    secciones = Seccion.objects.all()
    return render(request, 'inventario/secciones/seccion_lista.html', {'secciones': secciones})

@login_required
def formulario_seccion(request, id=None):
    if id:
        seccion = get_object_or_404(Seccion, id=id)
    else:
        seccion = None
    if request.method == 'POST':
        form = SeccionForm(request.POST, instance=seccion)
        if form.is_valid():
            form.save()
            return redirect('lista_secciones')
    else:
        form = SeccionForm(instance=seccion)
    return render(request, 'inventario/secciones/seccion_formulario.html', {'form': form})

@login_required
def eliminar_seccion(request, id):
    seccion = get_object_or_404(Seccion, id=id)
    if request.method == 'POST':
        seccion.delete()
    return redirect('lista_secciones')

# Views para Categoria
@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'inventario/secciones/categoria_lista.html', {'categorias': categorias})

@login_required
def formulario_categoria(request, id=None):
    if id:
        categoria = get_object_or_404(Categoria, id=id)
    else:
        categoria = None
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'inventario/secciones/categoria_formulario.html', {'form': form})

@login_required
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
    return redirect('lista_categorias')

# Views para Producto
@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/arreglos/producto_lista.html', {'productos': productos})

@login_required
def formulario_producto(request, id=None):
    if id:
        producto = get_object_or_404(Producto, id=id)
    else:
        producto = None
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventario/arreglos/producto_formulario.html', {'form': form})

@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
    return redirect('lista_productos')

# Views para Venta
@login_required
def lista_ventas(request):
    ventas = Venta.objects.all().order_by('-fecha')
    return render(request, 'inventario/ventas/venta_lista.html', {'ventas': ventas})

@login_required
def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            producto_id = request.POST.get('producto_id')
            cantidad = int(request.POST.get('cantidad', 0))
            if producto_id and cantidad > 0:
                producto = get_object_or_404(Producto, id=producto_id)
                if producto.stock >= cantidad:
                    venta.total = producto.precio * cantidad
                    venta.save()
                    DetalleVenta.objects.create(venta=venta, producto=producto, cantidad=cantidad, precio_unitario=producto.precio)
                    producto.stock -= cantidad
                    producto.save()
                    return redirect('lista_ventas')
                else:
                    form.add_error(None, "No hay suficiente stock")
    else:
        form = VentaForm()
    productos = Producto.objects.filter(stock__gt=0)
    return render(request, 'inventario/ventas/venta_formulario.html', {'form': form, 'productos': productos})

@login_required
def detalle_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    return render(request, 'inventario/ventas/venta_detalle.html', {'venta': venta})

# Views para Orden
@login_required
def lista_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'inventario/materiales/orden_lista.html', {'ordenes': ordenes})

@login_required
def formulario_orden(request, id=None):
    if id:
        orden = get_object_or_404(Orden, id=id)
    else:
        orden = None
    if request.method == 'POST':
        form = OrdenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('lista_ordenes')
    else:
        form = OrdenForm(instance=orden)
    return render(request, 'inventario/materiales/orden_formulario.html', {'form': form})

@login_required
def eliminar_orden(request, id):
    orden = get_object_or_404(Orden, id=id)
    if request.method == 'POST':
        orden.delete()
    return redirect('lista_ordenes')

# Views para Existencia
@login_required
def lista_existencias(request):
    existencias = Existencia.objects.all()
    return render(request, 'inventario/materiales/existencia_lista.html', {'existencias': existencias})

@login_required
def eliminar_existencia(request, id):
    existencia = get_object_or_404(Existencia, id=id)
    if request.method == 'POST':
        existencia.delete()
    return redirect('lista_existencias')

@login_required
def configurar_sitio(request):
    configuracion = Configuracion.objects.first()
    if not configuracion:
        configuracion = Configuracion.objects.create()
    if request.method == 'POST':
        form = ConfiguracionForm(request.POST, instance=configuracion)
        if form.is_valid():
            form.save()
            return redirect('configurar_sitio')
    else:
        form = ConfiguracionForm(instance=configuracion)
    return render(request, 'inventario/config/configuracion_formulario.html', {'form': form})

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'inventario/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('catalogo')

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'inventario/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('catalogo')
