from django.db import models

# Create your models here.

class Pagamento(models.Model):
    cpf = models.CharField(max_length=15)
    placa = models.CharField(max_length=15)
    statusPagamento = models.CharField(max_length=250)