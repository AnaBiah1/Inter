from rest_framework import serializers
from .models import Categoria, Aluno
class ModalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
class AlunoSerializer(serializers.ModelSerializer):
    modalidade = ModalidadeSerializer(read_only=True)
    modalidade_id = serializers.PrimaryKeyRelatedField(queryset=modalidade.objects,source='modalidade', write_only=True)
    class Meta:
        model = Aluno
        fields = '__all__'