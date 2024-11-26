from django.db import models

# Create your models here.
class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.TextField(max_length=255)
    calorias = models.IntegerField()
    proteina = models.IntegerField()
    carboidratos = models.IntegerField()
    gordura = models.IntegerField()
    sodio = models.IntegerField()
    acucar = models.IntegerField()
    sabores  = models.TextField(max_length=255)

    def __str__(self):
        return self.marca