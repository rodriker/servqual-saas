# servqual_saas/urls.py

from django.contrib import admin
from django.urls import path, include   # ← importa include

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path('api/v1/auth/', include('users.urls')),

    # SURVEYS + DIMENSIONS
    path('api/v1/', include('surveys.urls')),

    
]
