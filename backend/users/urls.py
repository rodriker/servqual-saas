from django.urls import path
from .views import SignupView
from .views import SignupView, CustomAuthToken

urlpatterns = [
    path('register/', SignupView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
]
