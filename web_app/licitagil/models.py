from django.db import models

# Create your models here.
class Licitacao(models.Model):
    numero = models.IntegerField(
        blank=False,
    )
    uasg = models.IntegerField(
        blank=False,
    )
    item = models.CharField(
        blank=False, 
        max_length=30,
    )
    cliente = models.CharField(
        blank=False, 
        max_length=50,
    )
    ganhou = models.BooleanField()
    data_pregao = models.DateField()
    data_entrega = models.DateField()

    def __str__(self):
        return self.item
