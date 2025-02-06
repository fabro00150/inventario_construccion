from django.shortcuts import render, redirect, get_object_or_404
from .models import Material, Suministrador, Orden, Existencia
from .forms import MaterialForm, SuministradorForm, OrdenForm


def base(request):
    return render(request, 'inventario/base.html')
# Views para Material
def lista_materiales(request):
    materiales = Material.objects.all()
    return render(request, 'inventario/lista_materiales.html', {'materiales': materiales})

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

    return render(request, 'inventario/formulario_material.html', {'form': form})

def eliminar_material(request, id):
    material = get_object_or_404(Material, id=id)
    if request.method == 'POST':
        material.delete()
        return redirect('lista_materiales')
    return render(request, 'inventario/confirmar_eliminar.html', {'object': material})

# Views para Suministrador
def lista_suministradores(request):
    suministradores = Suministrador.objects.all()
    return render(request, 'inventario/lista_suministradores.html', {'suministradores': suministradores})

def formulario_suministrador(request, id=None):
    if id:
        suministrador = get_object_or_404(Suministrador, id=id)
    else:
        suministrador = None

    if request.method == 'POST':
        form = SuministradorForm(request.POST, instance=suministrador)
        if form.is_valid():
            form.save()
            return redirect('lista_suministradores')
    else:
        form = SuministradorForm(instance=suministrador)

    return render(request, 'inventario/formulario_suministrador.html', {'form': form})

def eliminar_suministrador(request, id):
    suministrador = get_object_or_404(Suministrador, id=id)
    if request.method == 'POST':
        suministrador.delete()
        return redirect('lista_suministradores')
    return render(request, 'inventario/confirmar_eliminar.html', {'object': suministrador})

# Views para Orden
def lista_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'inventario/lista_ordenes.html', {'ordenes': ordenes})

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

    return render(request, 'inventario/formulario_orden.html', {'form': form})

def eliminar_orden(request, id):
    orden = get_object_or_404(Orden, id=id)
    if request.method == 'POST':
        orden.delete()
        return redirect('lista_ordenes')
    return render(request, 'inventario/confirmar_eliminar.html', {'object': orden})

# Views para Existencia
def lista_existencias(request):
    existencias = Existencia.objects.all()
    return render(request, 'inventario/lista_existencias.html', {'existencias': existencias})



def eliminar_existencia(request, id):
    existencia = get_object_or_404(Existencia, id=id)
    if request.method == 'POST':
        existencia.delete()
        return redirect('lista_existencias')
    return render(request, 'inventario/confirmar_eliminar.html', {'object': existencia})