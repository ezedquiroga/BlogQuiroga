from django.urls import path
from AppAdopcion.views import ofrecer_adopcion, editar_adopcion, home, MascotaDetalle
from django.views.generic.detail import DetailView

urlpatterns = [
    path('', home, name="home"),
    path('adopcion/', ofrecer_adopcion, name="AplicacionAdopcion"),
    path('detalles/', MascotaDetalle.as_view(), name="AplicacionDetalles"),
    path('adopcion/editar/<nombre>', editar_adopcion, name="AplicacionEditarAdopcion"),
]