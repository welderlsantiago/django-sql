from django.contrib import admin
from loja.models import Pedido, Produto 

# Register your models here.

admin.site.register(Pedido)
admin.site.register(Produto)