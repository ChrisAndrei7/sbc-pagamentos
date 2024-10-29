from rest_framework import serializers
from entities.vendas.vendasmodels import Venda

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'