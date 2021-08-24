from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Cliente, Barbearia, Servico, Ordem_Servico, Agenda
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = '__all__'

class BarbeariaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Barbearia
        fields = '__all__'

class ServicoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Servico
        fields = '__all__'

class OrdemServicoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Ordem_Servico
        fields = '__all__'

class AgendaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Agenda
        fields = '__all__'