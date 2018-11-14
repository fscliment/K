from django.contrib import admin
from app_portfolio.models import *

# Registre sus modelos aquí, para que aparezcan en la interfaz de administrador de Django.
admin.site.register(Perfil)
admin.site.register(Proyecto)
admin.site.register(Referencia)
admin.site.register(Experiencia)
admin.site.register(Reconocimiento)
