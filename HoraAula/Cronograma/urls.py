
from django.contrib import admin
from django.urls import path
from Cronograma import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path ('', views.index, name='index'),
    path ('horarios', views.horario_list, name='horario'),
    path ('horario/inserir', views.inserir, name='inserir'),
    path ('horario/inserir/salvar', views.salvar, name='salvar'),
    path ('horario/detalhe/<int:pk>', views.MateriaDetailView.as_view(), name='detalhe'),
    path ('horario/deletartudo',views.DeleteAll, name='deletarAll'),
] 


