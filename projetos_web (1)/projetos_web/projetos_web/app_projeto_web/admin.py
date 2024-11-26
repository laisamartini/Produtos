from django.contrib import admin
from .models import Produto
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('marca' , 'calorias' , 'proteina' , 'carboidratos' , 'gordura' , 'sodio' , 'acucar' , 'sabores')
admin.site.register(Produto, ProdutoAdmin)
# Register your models here.
