from django.shortcuts import render
from AppAdopcion.models import Mascota, Comentario
from AppAdopcion.forms import MascotaForm, ComentarioForm

def ofrecer_adopcion(request):
    all_mascotas = Mascota.objects.all()
    if request.method == "POST":
        mi_formulario = MascotaForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            mascota_save = Mascota(
                nombre=informacion['nombre'],
                edad=informacion['edad'],
                genero=informacion['genero'],
                vacunas=informacion['vacunas'],
                condicion_medica=informacion['condicio_medica'],
                castrado_a=informacion['castrado_a'],
                foto=informacion['foto']
            )
            mascota_save.save()
    context = {
        "mascotas": all_mascotas,
        "form": MascotaForm()
    }
    return render(request, "AppAdop/mascota.html", context=context)
