from django.contrib import admin

# Register your models here.
from licitagil.models import Licitacao, Tipo_compra, Tipo_envio 

admin.site.register(Tipo_compra)
admin.site.register(Tipo_envio)
admin.site.register(Licitacao)