from rest_framework import serializers
from .models import Encuesta, Pregunta

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = ['id', 'dimension', 'texto']

class EncuestaSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True, read_only=True)
    class Meta:
        model = Encuesta
        fields = ['id', 'titulo', 'creada', 'preguntas']

class EncuestaCreateSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True)

    class Meta:
        model = Encuesta
        fields = ['id', 'titulo', 'preguntas']

    def create(self, validated_data):
        preguntas_data = validated_data.pop('preguntas')
        encuesta = Encuesta.objects.create(**validated_data)
        for preg in preguntas_data:
            Pregunta.objects.create(encuesta=encuesta, **preg)
        return encuesta
