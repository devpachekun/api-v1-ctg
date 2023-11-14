from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'membresia', 'reservas_alta_demanda','is_staff', 'is_active', 'is_superuser']

    def create(self, validated_data):
        # Extrae la contraseña del validated_data
        password = validated_data.pop('password')

        # Crea un nuevo usuario sin guardar aún
        user = User(**validated_data)

        # Hashea y establece la contraseña
        user.set_password(password)

        # Guarda el usuario
        user.save()
        
        return user