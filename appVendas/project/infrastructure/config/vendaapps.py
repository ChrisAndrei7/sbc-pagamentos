from django.apps import AppConfig
from entities import vendas

class DjangoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vendas'
