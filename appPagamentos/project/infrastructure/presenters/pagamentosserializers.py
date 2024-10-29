from rest_framework import serializers
from entities.pagamentos.pagamentosmodels import Pagamento

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'