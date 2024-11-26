from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from django.http import HttpResponse

# Página inicial
def home(request):
    return render(request, 'cad_marca.html')

# Função para criar um novo produto (Marca)
def Marca(request):
    if request.method == "POST":
        nova_produto = Produto()
        nova_produto.marca = request.POST.get('marca')
        nova_produto.calorias = request.POST.get('calorias')
        nova_produto.proteina = request.POST.get('proteina')
        nova_produto.carboidratos = request.POST.get('carboidratos')
        nova_produto.gordura = request.POST.get('gordura')
        nova_produto.sodio = request.POST.get('sodio')
        nova_produto.acucar = request.POST.get('acucar')
        nova_produto.sabores = request.POST.get('sabores')
        nova_produto.save()
        return redirect('listagem_produtos')  # Redireciona após criar o produto
    return render(request, 'cad_marca.html')

# Função para listar todos os produtos
def listagem_produtos(request):
    lista_produtos = Produto.objects.all()
    return render(request, 'marca.html', {'produtos': lista_produtos})

# Função para editar um produto específico
def editar(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, "editar.html", {"produto": produto})

def update(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        produto.marca = request.POST.get("marca")
        produto.calorias = request.POST.get("calorias")
        produto.proteina = request.POST.get("proteina")
        produto.carboidratos = request.POST.get("carboidratos")
        produto.gordura = request.POST.get("gordura")
        produto.sodio = request.POST.get("sodio")
        produto.acucar = request.POST.get("acucar")
        produto.sabores = request.POST.get("sabores")
        
        produto.save()  # Salva as alterações no banco de dados
        return redirect('listagem_produtos')  # Redireciona para a listagem de produtos
    return render(request, "editar.html", {"produto": produto})

# Função para deletar um produto
def deletar(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('listagem_produtos')  # Redireciona após deletar o produto

