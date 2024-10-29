import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from entities.pagamentos.pagamentosmodels import Pagamento
from infrastructure.presenters.pagamentosserializers import PagamentoSerializer


@api_view(['GET'])
def getData(request):
    pagamentos = Pagamento.objects.all()
    serializer = PagamentoSerializer(pagamentos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPagamento(request, pk):
    pagamentos = Pagamento.objects.get(id=pk)
    serializer = PagamentoSerializer(pagamentos, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getPagamentoPlaca(request, placa):
    pagamentos = Pagamento.objects.get(placa=placa)
    serializer = PagamentoSerializer(pagamentos, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getPagamentoCPF(request, cpf):
    pagamentos = Pagamento.objects.get(cpf=cpf)
    serializer = PagamentoSerializer(pagamentos, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addPagamento(request):
    serializer = PagamentoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updatePagamento(request, pk):
    pagamento = Pagamento.objects.get(id=pk)
    serializer = PagamentoSerializer(instance=pagamento, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deletePagamento(request, pk):
    pagamento = Pagamento.objects.get(id=pk)
    pagamento.delete()
    return Response('Pagamento deletado com sucesso!')
