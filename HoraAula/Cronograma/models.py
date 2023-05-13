from django.db import models

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200,null=False, help_text="Nome do Professor" )
    nome_abreviado = models.CharField(verbose_name="NomeAbreviado", max_length=50, null=False, help_text="Nome Abreviado do Professor")
    cpf = models.CharField(verbose_name="CPF",null=False, max_length = 14, help_text="CPF do professor")
    endereco = models.CharField(verbose_name="Endereco",null=False, max_length=100, help_text="Endereço do professor: Rua e Numero")
    cidade = models.CharField(verbose_name="Cidade", max_length=100,null=False, help_text="Cidade do professor")
    estado = models.CharField(verbose_name="Estado",max_length=2,null=False,help_text="Sigla do estado")
    cep = models.CharField(verbose_name="CEP",max_length=8,null=False, help_text="Cep da cidade do professor")

    def __str__(self):
        return self.nome
    
class Materia(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200, null=False, blank=False,help_text="Nome da materia" )
    descricao = models.CharField(verbose_name="Descricao", max_length=2000, null=False, blank=False, help_text="Descreva a materia")
    curso = models.CharField(verbose_name="Curso", max_length=50, null=False,blank=False,help_text="Curso da materia")
    semestre = models.IntegerField(verbose_name="Semestre", null=False, help_text="Numero do semestre que é a materia")
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        verbose_name="Professor",
        null=False,
        help_text="Materia que o professor ensina"
    )

    def __str__(self):
        return self.nome

class Horario(models.Model):
    dia = models.CharField(verbose_name="Dia", max_length=200, null=False, blank=False,help_text="Dia da semana da disciplina" )
    horario = models.CharField(verbose_name="horario",max_length=20, null=False, blank=False,help_text="Horario da disciplina")
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        verbose_name="Professor",
        null=False,
        help_text="horario da aula do professor"
    )
    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        verbose_name="Materia",
        null=False,
        help_text="horario da materia"
    )
    def __str__(self):
        return self.horario+self.dia