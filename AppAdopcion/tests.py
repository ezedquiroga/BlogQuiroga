from django.test import TestCase
from django.urls import reverse
from AppAdopcion.models import Mascota

class MascotaTestCase(TestCase):
    def setUp(self):
        Mascota.objects.create(nombre="Pepe", edad=4)
        Mascota.objects.create(nombre="Lola", edad=2)

    def test_creando_mascota(self):
        p1 = Mascota.objects.get(edad=4)
        p2 = Mascota.objects.get(edad=2)
        self.assertEqual(p1.nombre, 'Pepe')
        self.assertEqual(p2.nombre, 'Lola')

class ViewTest(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Necesitamos que se registre")

    def test_past_question(self):
        mascota = Mascota.objects.create(nombre="Pepe", edad=4)
        response = self.client.get(reverse('AplicacionAdopcion'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            f"mascota: Pepe edad: 4"
        )