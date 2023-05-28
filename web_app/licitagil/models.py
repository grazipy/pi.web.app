from django.db import models

# Create your models here.
class Tipo_compra(models.Model):
    tipo_compra = models.CharField(
        blank=False,
        max_length=20,
    )

    def __str__(self):
        return self.tipo_compra


class Tipo_envio(models.Model):
    tipo_envio = models.CharField(
        blank=False,
        max_length=10,
    )

    def __str__(self):
        return self.tipo_envio


class Licitacao(models.Model):
    uasg = models.IntegerField(blank=False)
    cliente = models.CharField(
        blank=False, 
        max_length=50,
    )
    local_entrega = models.CharField(
        blank=False, 
        max_length=30,
    )
    equipamento = models.CharField(
        blank=False, 
        max_length=30,
    )
    tipo_compra = models.ForeignKey(Tipo_compra, on_delete=models.SET_NULL, null=True)
    tipo_envio = models.ForeignKey(Tipo_envio, on_delete=models.SET_NULL, null=True)
    disputa = models.BooleanField()
    ganhou = models.BooleanField()
    data_disputa = models.DateField()
    documentos = models.CharField(
        blank=False, 
        max_length=50,
    )

    def __str__(self):
        return self.equipamento

