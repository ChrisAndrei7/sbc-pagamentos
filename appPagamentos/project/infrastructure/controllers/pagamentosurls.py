from django.urls import path
from application.usecases import pagamentosviews

urlpatterns = [
    path('', pagamentosviews.getData),
    path('create', pagamentosviews.addPagamento),
    path('read/<str:pk>', pagamentosviews.getPagamento),
    path('readCPF/<str:cpf>', pagamentosviews.getPagamentoCPF),
    path('readplaca/<str:placa>', pagamentosviews.getPagamentoPlaca),
    path('update/<str:pk>', pagamentosviews.updatePagamento),
    path('delete/<str:pk>', pagamentosviews.deletePagamento),
]
