from django.test import TestCase
from django.urls import reverse
from .models import Producto, Configuracion, Seccion

class RoseShopTests(TestCase):
    def setUp(self):
        Configuracion.objects.create(nombre_sitio="Rose Shop", whatsapp="12345")
        self.seccion = Seccion.objects.create(nombre="Arreglos Florales")
        self.producto = Producto.objects.create(
            nombre="Rosa Test",
            descripcion="Test",
            precio=100.0,
            stock=5,
            seccion=self.seccion
        )

    def test_catalogo_view(self):
        response = self.client.get(reverse('catalogo'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rosa Test")

    def test_admin_views_redirect_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
