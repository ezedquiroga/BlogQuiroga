from django.shortcuts import render
from AppAdopcion.models import Mascota, Comentario
from AppAdopcion.forms import OfrecerAdopcionForm, ComentarioForm


def home(request):
    return render(request, "base.html")


def ofrecer_adopcion(request):
    all_mascotas = Mascota.objects.all()
    if request.method == "POST":
        mi_formulario = OfrecerAdopcionForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            mascota_save = Mascota(
                nombre=informacion['nombre'],
                edad=informacion['edad'],
                genero=informacion['genero'],
                vacunas=informacion['vacunas'],
                condicion_medica=informacion['condicion_medica'],
                castrado_a=informacion['castrado_a']
            )
            mascota_save.save()
    context = {
        "mascotas": all_mascotas,
        "form": OfrecerAdopcionForm()
    }
    return render(request, "AppAdop/ofrecer_adopcion.html", context=context)
