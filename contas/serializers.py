from rest_framework import serializers

from contas.models import Transacao, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    nome: serializers.CharField(max_length=200)
    dt_criacao: serializers.DateTimeField()

    class Meta:
        model = Categoria
        fields = ['nome', 'dt_criacao']


class ControleGastosListViewSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    descricao = serializers.CharField(max_length=200)
    valor = serializers.DecimalField(max_digits=7, decimal_places=2)
    data = serializers.DateTimeField()

    class Meta:
        model = Transacao
        fields = ['id', 'descricao', 'valor', 'data']


class ControleGastosViewSerializer(serializers.Serializer):
    data = serializers.DateTimeField()
    valor = serializers.DecimalField(max_digits=7, decimal_places=2)
    #categoria = CategoriaSerializer(many=False)
    descricao = serializers.CharField(max_length=200)

    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor']

    def create(self, validated_data):
        return Transacao.objects.create(**validated_data)
