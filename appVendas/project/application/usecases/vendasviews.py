import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from entities.vendas.vendasmodels import Venda
from infrastructure.presenters.vendasserializers import VendaSerializer


@api_view(['GET'])
def getData(request):
    vendas = Venda.objects.all()
    serializer = VendaSerializer(vendas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getVenda(request, pk):
    vendas = Venda.objects.get(id=pk)
    serializer = VendaSerializer(vendas, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getVendaPlaca(request, placa):
    vendas = Venda.objects.get(placa=placa)
    serializer = VendaSerializer(vendas, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getVendaCPF(request, cpf):
    vendas = Venda.objects.get(cpf=cpf)
    serializer = VendaSerializer(vendas, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addVenda(request):
    serializer = VendaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateVenda(request, pk):
    venda = Venda.objects.get(id=pk)
    serializer = VendaSerializer(instance=venda, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteVenda(request, pk):
    venda = Venda.objects.get(id=pk)
    venda.delete()
    return Response('Venda deletada com sucesso!')
