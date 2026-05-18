from django import forms
from .models import Material, Orden, Existencia, Categoria, Producto, Venta, Configuracion, Seccion

class SeccionForm(forms.ModelForm):
    class Meta:
        model = Seccion
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'seccion': forms.Select(attrs={'class': 'select2 form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'unidad_medida' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio_unitario' : forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control', 'id': 'foto'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'stock' : forms.NumberInput(attrs={'class': 'form-control'}),
            'seccion': forms.Select(attrs={'class': 'select2 form-control'}),
            'categoria': forms.Select(attrs={'class': 'select2 form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control', 'id': 'foto_producto'}),
        }

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente_nombre', 'metodo_pago']
        widgets = {
            'cliente_nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'metodo_pago' : forms.Select(attrs={'class': 'form-control'}),
        }

class ConfiguracionForm(forms.ModelForm):
    class Meta:
        model = Configuracion
        fields = '__all__'
        widgets = {
            'nombre_sitio' : forms.TextInput(attrs={'class': 'form-control'}),
            'color_primario' : forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'color_secundario' : forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'whatsapp' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'
        widgets = {
            'material': forms.Select(attrs={'class': 'select2 form-control'}),
            'cantidad' : forms.TextInput(attrs={'class': 'form-control'}),        
        }

class ExistenciaForm(forms.ModelForm):
    class Meta:
        model = Existencia
        fields = '__all__'
