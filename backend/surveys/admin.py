from django.contrib import admin
from .models import Dimension, Encuesta, Pregunta, Respuesta

admin.site.register(Dimension)
admin.site.register(Encuesta)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
