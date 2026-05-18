from .models import Configuracion

def config_processor(request):
    config = Configuracion.objects.first()
    if not config:
        config = Configuracion.objects.create(nombre_sitio="Palo de Rosa", whatsapp="573000000000")
    return {'config': config}
