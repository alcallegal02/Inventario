from rest_framework import serializers
from .models import Equipo, Impresora, Nave, Trabajador, Departamento  # Asegúrate de importar todo lo necesario

# Definición del serializador para Impresora
class ImpresoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impresora
        fields = '__all__'  # Solo incluye los campos necesarios

# Definición del serializador para Equipo
class EquipoSerializer(serializers.ModelSerializer):
    impresoras = ImpresoraSerializer(many=True, read_only=True)  # Relación con impresoras

    class Meta:
        model = Equipo
        fields = '__all__'  # O puedes definir los campos explícitamente si lo prefieres

# Otros serializadores
class NaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nave
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class TrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = '__all__'
