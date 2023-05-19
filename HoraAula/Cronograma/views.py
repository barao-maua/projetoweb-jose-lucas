from django.shortcuts import render 
from django.http import HttpResponse 
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Horario

def index(request): 
    return render(request, 'index.html')


class HorarioListView(generic.ListView):
    model = Horario
    template_name = 'horario.html'
    context_object_name = 'horario'

class HorarioCreateView(generic.CreateView):
    model = Horario
    template_name = 'create.html'
    context_object_name = 'horario'