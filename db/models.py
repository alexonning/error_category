from django.db import models

class AutomacaoNew(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='id')
    projeto_nome = models.CharField(max_length=255)
    schema = models.CharField(max_length=255)
    nome_tabela = models.CharField(max_length=255)

    
    class Meta:
        managed = False
        db_table = '"sustentacao"."automacao_new"'
        verbose_name = 'Automação New'

    def __str__(self):
        return self.projeto_nome
    
class TarefaNew(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_automacao = models.ForeignKey(AutomacaoNew, on_delete=models.PROTECT, db_column='id_automacao')
    # Outros campos relevantes da tabela tarefa_new
    
    class Meta:
        managed = False
        db_table = '"sustentacao"."tarefa_new"'
        verbose_name = 'Tarefa New'

    def __str__(self):
        return self.id

# Create your models here.
class RoboNew(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.TextField(verbose_name='Descrição')

    class Meta:
        managed = False
        db_table = '"sustentacao"."robo_new"'
        verbose_name = 'Robo New'
        

class SituacaoAutomacao(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.TextField(verbose_name='Descrição')

    class Meta:
        managed = False
        db_table = '"sustentacao"."situacao_automacao"'
        verbose_name = 'Situação Automação'