from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from exercicios.models import Exercicio
from exercicios.serializers import ExercicioSerializer

class ListaExercicisView(APIView):

    def get(self, request):
        exercicios = Exercicio.objects.all()
        serializer = ExercicioSerializer(exercicios, many=True)
        return Response(serializer.data, status=200)
    def post(self, request):
        serializer = ExercicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)