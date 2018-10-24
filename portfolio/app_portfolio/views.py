from django.shortcuts import render
from app_portfolio.models import *
from django.core.mail import send_mail

# Agregue sus vistas (el equivalente el Controlador en un modelo MVC) aquí
from butter_cms import ButterCMS
def portfolio(request):

    """Inicializamos un diccionario que servirá como variable del contexto, dentro de la cual estaran todas las variables
       creadas para contener cada objeto"""

    contexto = {}
    # Obteniendo los objetos de la base de datos e ingresandolos a la variable contexto.
    contexto['perfil'] = Perfil.objects.first()
    contexto['proyectos'] = Proyecto.objects.all()
    contexto['referencias'] = Referencia.objects.all()
    contexto['habilidades'] = Experiencia.objects.filter(tipo='1')
    contexto['conocimientos'] = Experiencia.objects.filter(tipo='2')
    contexto['reconocimientos'] = Reconocimiento.objects.all()

    for proyecto in contexto['proyectos']:
        if proyecto.tags:
            proyecto.tags = proyecto.tags.replace(' ', '').split(',')

    # Si se realiza un post desde la template, se entiende que se enviara el correo
    if request.method == 'POST':
        mail = 'kinetia@kinetia.ch'    # Correo electronico de la persona que lo envia (Esta configurado en setting.py)
        email = request.POST.get('email')  # Correo que ingresa el visitante de la pagina
        mensaje = request.POST.get('message')
        nombre = request.POST.get('name')
        tema = request.POST.get('subject')
        receptor = ['kinetia@kinetia.ch'] # Correo al cual se envia el mensaje
        cuerpo_mensaje = nombre + "\n" + email + "\n\n\n" + mensaje
    # Funcion propia de Django para envio de correos
        send_mail(
            tema,
            cuerpo_mensaje,
            mail,
            receptor,
            fail_silently=False,
        )

    return render(request, 'portfolio.html', contexto)

def checkDevice(request):
    
    """Función para identificar el dispositivo y configurar vistas"""
    
    
    if request.mobile:
        is_mobile = True
    else:
        is_mobile = False

    context = {
        
        'is_mobile': is_mobile,
    }
    return render(request, 'mytemplate.html', context)


    
    