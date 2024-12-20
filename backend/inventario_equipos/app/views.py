from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Departamento, Nave, Trabajador, Equipo, Impresora
from .serializers import DepartamentoSerializer, NaveSerializer, TrabajadorSerializer, EquipoSerializer, ImpresoraSerializer

class NaveViewSet(viewsets.ModelViewSet):
    queryset = Nave.objects.all()
    serializer_class = NaveSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

    @action(detail=False, methods=['get'])
    def by_nave(self, request):
        nave_id = request.query_params.get('nave', None)

        if nave_id:
            try:
                departamentos = Departamento.objects.filter(nave_id=nave_id)
                serializer = DepartamentoSerializer(departamentos, many=True)
                return Response(serializer.data)
            except Exception as e:
                print("Error al filtrar los departamentos:", e)
                return Response([])
        return Response([])



class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer

    @action(detail=False, methods=['get'])
    def by_departamento(self, request):
        departamento_id = request.query_params.get('departamento', None)

        if departamento_id:
            try:
                trabajadores = Trabajador.objects.filter(departamento_id=departamento_id)
                serializer = TrabajadorSerializer(trabajadores, many=True)
                return Response(serializer.data)
            except Exception as e:
                print("Error al filtrar los trabajadores:", e)
                return Response([])
        return Response([])


class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


class ImpresoraViewSet(viewsets.ModelViewSet):
    queryset = Impresora.objects.all()
    serializer_class = ImpresoraSerializer

    @action(detail=False, methods=['get'])
    def by_departamento(self, request):
        departamento_id = request.query_params.get('departamento', None)

        if departamento_id:
            try:
                impresoras = Impresora.objects.filter(departamento_id=departamento_id)
                serializer = ImpresoraSerializer(impresoras, many=True)
                return Response(serializer.data)
            except Exception as e:
                print("Error al filtrar los impresoras:", e)
                return Response([])  # En caso de error, devuelve un array vacío
        return Response([])