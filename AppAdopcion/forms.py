from django import forms
from AppAdopcion.models import Mascota, Comentario

class OfrecerAdopcionForm(forms.Form):

    nombre = forms.CharField(max_length=15)
    edad = forms.CharField(max_length=8)
    genero = forms.CharField(max_length=6)
    vacunas = forms.CharField(max_length=20)
    condicion_medica = forms.CharField(max_length=20)
    castrado_a = forms.CharField(max_length=2)
    foto = forms.ImageField()


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ( 'nombre', 'mensaje' )
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensqaje': forms.Textarea(attrs={'class': 'form-control'}),
        }