from django.urls import path
from application.usecases import vendasviews

urlpatterns = [
    path('', vendasviews.getData),
    path ('create', vendasviews.addVenda),
    path ('read/<str:pk>', vendasviews.getVenda),
    path ('readCPF/<str:cpf>', vendasviews.getVendaCPF),
    path('readplaca/<str:placa>', vendasviews.getVendaPlaca),
    path ('update/<str:pk>', vendasviews.updateVenda),
    path ('delete/<str:pk>', vendasviews.deleteVenda),
]
