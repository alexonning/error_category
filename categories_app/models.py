from django.db import models
from db.models import SituacaoRotina, RoboNew

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, verbose_name='Nome')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    requires_description = models.BooleanField(default=False, blank=False, null=False, verbose_name='Requer Descrição')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = "Categorias"
        ordering = ['name']


class ErrorCategory(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    Category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='error_categories', blank=False, null=True, verbose_name='Categoria   ')
    id_error = models.BigIntegerField(verbose_name='ID do erro', blank=True, null=True)
    affected_table = models.TextField(verbose_name='Tabela Afetada', blank=True, null=True)
    situation = models.ForeignKey(SituacaoRotina, on_delete=models.PROTECT, verbose_name='Situação Rotina', blank=True, null=True)
    description_error = models.TextField(blank=True, null=True, verbose_name='Descrição do Erro')
    date_hour = models.DateTimeField(verbose_name='Data e Hora do registro', blank=True, null=True)
    routine_id = models.BigIntegerField(verbose_name='ID da Rotina', blank=True, null=True)
    robot = models.ForeignKey(RoboNew, on_delete=models.PROTECT, verbose_name='Robo', blank=True, null=True)
    extra_data = models.JSONField(verbose_name='Dados Extras', blank=True, null=True)
    
    
    def __str__(self):
        return f"{str(self.id)} - {self.description}"

    class Meta:
        verbose_name = 'Erro Categorizado'
        verbose_name_plural = "Erros Categorizados"
        # ordering = ['date_hour']