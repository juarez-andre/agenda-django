from django.shortcuts import get_object_or_404, redirect, render
from agenda.models import Compromisso
from agenda.forms import CompromissoForm

# Create your views here.
def listagem(request):
    if request.user.is_authenticated:
        context = {}
        compromissos = Compromisso.objects.all().order_by('-data')
        context['compromissos'] = compromissos
        return render(request, 'agenda/listagem.html', context)
    else:
        redirect('accounts/login')
    
def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CompromissoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('../')
            else:
                return render(request, 'agenda/create.html', {'form': form})
        else:
            form = CompromissoForm()
            return render(request, 'agenda/create.html', {'form': form})
    else:
        return redirect('login')

def delete(request, compromisso_id):
    objeto = Compromisso.objects.get(pk=compromisso_id)
    objeto.delete()
    return redirect('../')

