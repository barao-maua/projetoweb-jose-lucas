from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Horario,Professor, Materia

def index(request): 
    return render(request, 'index.html')

def inserir(request):
    professor = Professor.objects.all()
    materias = Materia.objects.all()
    return render(request, "create.html",{'materias': materias,'professores':professor})

def salvar(request):
    dia = request.POST.get("dia")
    # variaveis para o primeiro horário
    horario1 = "19:10 - 20:00"
    prof1 = request.POST.get("nome-professor1")
    professor1 = Professor.objects.get(id = prof1)
    mat1 = request.POST.get("nome-materia1")
    materia1 = Materia.objects.get(id = mat1)
    Horario.objects.create(dia=dia, horario=horario1, 
                           professor=professor1, 
                           materia=materia1)
    horario2 = "20:00 - 20:50"
    prof2 = request.POST.get("nome-professor2")
    professor2 = Professor.objects.get(id = prof2)
    mat2 = request.POST.get("nome-materia2")
    materia2 = Materia.objects.get(id = mat2)
    Horario.objects.create(dia=dia, horario=horario2, 
                           professor=professor2, 
                           materia=materia2)
    horario3 = "21:05 - 21:55"
    prof3 = request.POST.get("nome-professor3")
    professor3 = Professor.objects.get(id = prof3)
    mat3 = request.POST.get("nome-materia3")
    materia3 = Materia.objects.get(id = mat3)
    Horario.objects.create(dia=dia, horario=horario3, 
                           professor=professor3, 
                           materia=materia3)
    horario4 = "21:55 - 22:45"
    prof4 = request.POST.get("nome-professor4")
    professor4 = Professor.objects.get(id = prof4)
    mat4 = request.POST.get("nome-materia4")
    materia4 = Materia.objects.get(id = mat4)
    Horario.objects.create(dia=dia, horario=horario4, 
                           professor=professor4, 
                           materia=materia4)
    horario_all = Horario.objects.all()
    
    return redirect(horario_list)

def DeleteAll(request):
    horario= Horario.objects.all()
    horario.delete()
    horario_all = Horario.objects.all()
    return render(request,"horario.html",{'horario_list':horario_all})

# def delete(request):
#     button1 = request.POST.get("button1")
#     button2 = request.POST.get("button2")
#     button3 = request.POST.get("button3")
#     button4 = request.POST.get("button4")
#     if (button1 == 1){

#     }
#     if (button2 == 1){

#     }
#     if(button3 == 1){

#     }
#     if(button4 == 1 ){

#     }
#     return redirect(horario_list)

def deleteDia(request):
    horario_all = Horario.objects.all()
    dia = request.POST.get("escolha-dia")
    return render(request,"delete.html",{'delete_list':horario_all,'dia_semana':dia})
    

def horario_list(request):
    horario_all = Horario.objects.all()
    return render(request,"horario.html",{'horario_list':horario_all})