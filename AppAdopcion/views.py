from django.shortcuts import render, redirect
from AppAdopcion.models import Mascota, Comentario
from AppAdopcion.forms import OfrecerAdopcionForm, ComentarioForm
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def home(request):
    return render(request, "base.html")


def ofrecer_adopcion(request):
    all_mascotas = Mascota.objects.all()
    if request.method == "POST":
        mi_formulario = OfrecerAdopcionForm(request.POST, request.FILES)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            mascota_save = Mascota(
                nombre=informacion['nombre'],
                edad=informacion['edad'],
                genero=informacion['genero'],
                vacunas=informacion['vacunas'],
                condicion_medica=informacion['condicion_medica'],
                castrado_a=informacion['castrado_a'],
                foto=informacion['foto']
            )
            mascota_save.save()
    context = {
        "mascotas": all_mascotas,
        "form": OfrecerAdopcionForm()
    }
    return render(request, "AppAdop/ofrecer_adopcion.html", context=context)


def editar_adopcion(request, nombre):
    get_adopcion = Mascota.objects.get(nombre=nombre)

    if request.method == "POST":
        mi_formulario = OfrecerAdopcionForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            get_adopcion.nombre = informacion['nombre']

            get_adopcion.save()
            return redirect("AplicacionAdopcion")

    context = {
        "nombre": nombre,
        "form": OfrecerAdopcionForm(initial={
            "nombre": get_adopcion.nombre
        })
    }
    return render(request, "AppAdop/editar_adopcion.html", context=context)


class ComentarioView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'AppAdop/comentario.html'
    success_url = reverse_lazy('AplicacionAdopcion')

    def form_valid(self, form1):
        form1.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioView, self).form_valid(form1)

class MascotaDetalle(LoginRequiredMixin, DetailView):
    model = Mascota
    context_object_name = 'mascota'
    template_name = 'AppAdop/detalles.html'
