from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dimension
from .serializers import EncuestaCreateSerializer

class HelloWorld(APIView):
    def get(self, request, version):
        return Response({"message": "Hello, world!"})

class ListDimensions(APIView):
    def get(self, request, version):
        dims = list(Dimension.objects.values("id", "nombre", "descripcion"))
        return Response(dims)

from rest_framework import generics
from .models import Encuesta
from .serializers import EncuestaSerializer

class EncuestaListCreate(generics.ListCreateAPIView):
    queryset = Encuesta.objects.all().order_by('-creada')
    serializer_class = EncuestaSerializer

class EncuestaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer
    lookup_field = 'id'

class EncuestaFullCreate(generics.CreateAPIView):
    serializer_class = EncuestaCreateSerializer