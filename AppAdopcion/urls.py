from django.urls import path
from AppAdopcion.views import ofrecer_adopcion, editar_adopcion, home

urlpatterns = [
    path('', home, name="home"),
    path('adopcion/', ofrecer_adopcion, name="AplicacionAdopcion"),
    path('adopcion/editar/<nombre>', editar_adopcion, name="AplicacionEditarAdopcion"),
]