from .models import Configuracion

def config_processor(request):
    config = Configuracion.objects.first()
    if not config:
        config = Configuracion.objects.create()
    return {'config': config}
