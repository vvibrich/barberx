"""BarberX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from api.views import BarbeariaList, ClienteList, ServicoList, OrdemServicoList, MyObtainTokenPairView, RegisterView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'barbearias', BarbeariaList, basename='Barber')
router.register(r'clientes', ClienteList, basename='Cliente')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    url(r'^barbearias/$', BarbeariaList.as_view(), name='barber-list'),
    url(r'^clientes/$', ClienteList.as_view(), name='cliente-list'),
    url(r'^servicos/$', ServicoList.as_view(), name='servico-list'),
    url(r'^ordem-servico/$', OrdemServicoList.as_view(), name='ordem-servico-list')
]
