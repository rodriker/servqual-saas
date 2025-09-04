from django.db import models

class Dimension(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

class Encuesta(models.Model):
    titulo = models.CharField(max_length=200)
    creada = models.DateTimeField(auto_now_add=True)

class Pregunta(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, related_name="preguntas")
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    texto = models.CharField(max_length=300)

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name="respuestas")
    expectativa = models.IntegerField()
    percepcion = models.IntegerField()
