from django.shortcuts import render
from rest_framework import generics
from .models import Cliente, Barbearia, Servico, Ordem_Servico
from .serializers import ClienteSerializer, BarbeariaSerializer, ServicoSerializer, OrdemServicoSerializer, MyTokenObtainPairSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

# Create your views here.
class ClienteList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,) 
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class BarbeariaList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Barbearia.objects.all()
    serializer_class = BarbeariaSerializer

class ServicoList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class OrdemServicoList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Ordem_Servico.objects.all()
    serializer_class = OrdemServicoSerializer
