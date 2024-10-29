from django.db import models

# Create your models here.

class Venda(models.Model):
    cpf = models.CharField(max_length=15)
    placa = models.CharField(max_length=15)
    NomeCliente = models.CharField(max_length=250)
    veiculo = models.CharField(max_length=250)
    dataVenda = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
