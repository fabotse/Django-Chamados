from django.shortcuts import render,redirect
from django.http import HttpResponse

from chamados.forms import ChamadoForm
from .models import Chamado

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def home(request):
    chamados = Chamado.objects.all()
    context = {'chamados' : chamados}
    return render(request, 'chamados/home.html', context)


def chamado(request,pk):
    chamadoObj = Chamado.objects.get(id=pk)
    
    return render(request, 'chamados/chamados.html', {'chamadoObj' : chamadoObj})


def create_chamado(request):
    form = ChamadoForm()

    if request.method == 'POST':
        form = ChamadoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'chamados/chamado_form.html', context)


def update_chamado(request, pk):

    chamado = Chamado.objects.get(id=pk)
    form = ChamadoForm(instance=chamado)
    
    if request.method == 'POST':
        form = ChamadoForm(request.POST, instance=chamado)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'chamados/chamado_form.html', context)

def delete_chamado(request, pk):
    
    chamado = Chamado.objects.get(id=pk)
    context = {'object' : chamado}
    if request.method == 'POST':
        chamado.delete()
        return redirect('home')

    return render(request,'chamados/delete_template.html', context)