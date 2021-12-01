from rest_framework import serializers, viewsets
from Escola.models import Aluno
from Escola.serializer import AlunoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    