from django.urls import path
from .views import (
    HelloWorld,
    ListDimensions,
    EncuestaListCreate,
    EncuestaDetail,
    EncuestaFullCreate,    # ← Importa la vista anidada
)

urlpatterns = [
    path('<str:version>/hello/', HelloWorld.as_view(), name='hello-world'),
    path('<str:version>/dimensions/', ListDimensions.as_view(), name='list-dimensions'),

    # — CRUD simple de encuestas —
    path('<str:version>/surveys/', EncuestaListCreate.as_view(), name='survey-list'),
    path('<str:version>/surveys/<int:id>/', EncuestaDetail.as_view(), name='survey-detail'),

    # — Crear encuesta con preguntas en un solo POST —
    path('<str:version>/surveys-full/', EncuestaFullCreate.as_view(), name='survey-full-create'),
]
