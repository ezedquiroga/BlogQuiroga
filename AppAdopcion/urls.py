from django.urls import path
from AppAdopcion.views import ofrecer_adopcion

urlpatterns = [
    path('adopcion/', ofrecer_adopcion, name="AplicacionAdopcion"),
]