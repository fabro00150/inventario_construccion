from django import forms
from .models import Material, Suministrador, Orden, Existencia

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'unidad_medida' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio_unitario' : forms.TextInput(attrs={'class': 'form-control'}),
            'suministrador': forms.Select(attrs={'class': 'select2 form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control', 'id': 'foto'}),
        }

class SuministradorForm(forms.ModelForm):
    class Meta:
        model = Suministrador
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),        
            'direccion' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            
        }

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'
        widgets = {
            'material': forms.Select(attrs={'class': 'select2 form-control'}),
            'cantidad' : forms.TextInput(attrs={'class': 'form-control'}),        
            'suministrador': forms.Select(attrs={'class': 'select2 form-control'}),
        }

class ExistenciaForm(forms.ModelForm):
    class Meta:
        model = Existencia
        fields = '__all__'