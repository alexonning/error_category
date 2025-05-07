from pyexpat import model
from django.db import models

ATIVO_INATIVO = [
    ('T', 'T'),
    ('F', 'F'),
]

PRIORITY = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
]


class SituacaoAutomacao(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name='ID')
    description = models.TextField(verbose_name='Descrição', db_column='descricao')
        
    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = '"sustentacao"."situacao_automacao"'
        verbose_name = 'Situação Automação'
        verbose_name_plural = 'Situação Automações'


class SituacaoRobo(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name='ID')
    description = models.TextField(verbose_name='Descrição', db_column='descricao')
    observation = models.TextField(verbose_name='Descrição', db_column='obs')
        
    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = '"sustentacao"."situacao_robo"'
        verbose_name = 'Situação Robô'
        verbose_name_plural = 'Situação Robôs'


class SituacaoRotina(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name='ID')
    description = models.TextField(verbose_name='Descrição', db_column='descricao')

    
    def __str__(self):
        return self.description
    
    class Meta:
        managed = False
        db_table = '"sustentacao"."situacao_rotina"'
        verbose_name = 'Situação Rotina'
        verbose_name_plural = 'Situação Rotinas'


class Projeto(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=255, db_column='nome', verbose_name='Nome')
    area = models.CharField(max_length=255, db_column='area', verbose_name='Area')

    class Meta:
        managed = False
        db_table = '"sustentacao"."projeto"'
        verbose_name = 'Projeto'
        
    def __str__(self):
        return self.name


class AutomacaoNew(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='id')
    situation = models.ForeignKey(SituacaoAutomacao, on_delete=models.PROTECT, db_column='id_situacao', verbose_name='Situação', null=False, blank=False)
    project = models.ForeignKey(Projeto, on_delete=models.PROTECT, db_column='id_projeto', verbose_name='Projeto', null=False, blank=False)
    task_unique = models.CharField(max_length=1, db_column='tarefa_unica', verbose_name='Tarefa Única', choices=ATIVO_INATIVO, null=False, blank=False)
    indeed = models.CharField(max_length=255, db_column='alias', verbose_name='Alias', null=False, blank=False)
    description = models.TextField(db_column='descricao', verbose_name='Descrição', null=False, blank=False)
    priority = models.CharField(max_length=255, db_column='prioridade', verbose_name='Prioridade', choices=PRIORITY, null=False, blank=False)
    business_day_only = models.CharField(max_length=1, db_column='somente_dia_util', verbose_name='Somente dia útil', choices=ATIVO_INATIVO, null=False, blank=False)
    executor_time = models.BigIntegerField(db_column='tempo_executor', verbose_name='Tempo Executor', null=False, blank=False)
    median_executor_time = models.DecimalField(max_digits=10, decimal_places=2, db_column='custo_executor_mediana', verbose_name='Tempo Executor Mediana', null=False, blank=False)
    average_executor_time = models.DecimalField(max_digits=10, decimal_places=2, db_column='custo_executor_media', verbose_name='Custo Executor Média', null=False, blank=False)
    robot_cost = models.DecimalField(max_digits=10, decimal_places=2, db_column='custo_robo', verbose_name='Custo Robô', null=False, blank=False)
    sla_wait = models.IntegerField(db_column='sla_espera', verbose_name='SLA Espera', null=False, blank=False)
    sla_execution = models.IntegerField(db_column='sla_execucao', verbose_name='SLA Execução', null=False, blank=False)
    average_execution_time = models.IntegerField(db_column='tempo_medio_execucao', verbose_name='Tempo Médio Execução', null=False, blank=False)
    maximum_average_execution_time = models.IntegerField(db_column='tempo_medio_maximo_execucao', verbose_name='Tempo Médio Máximo Execução', null=False, blank=False)
    maximum_average_execution_time = models.IntegerField(db_column='tempo_medio_maximo_execucao', verbose_name='Tempo Médio Máximo Execução', null=False, blank=False)
    limit_attempts = models.IntegerField(db_column='limite_tentativas', verbose_name='Limite Tentativas', null=False, blank=False)
    action_protocol = models.IntegerField(db_column='acao_protocolo', verbose_name='Ação Protocolo')
    action_return = models.IntegerField(db_column='acao_devolucao', verbose_name='Ação Devolução')
    robot_limits = models.IntegerField(db_column='limite_robos', verbose_name='Limite Robôs', null=False, blank=False)
    quick_task_calculation = models.IntegerField(db_column='calculo_tarefa_rapida', verbose_name='Calculo Tarefa Rápida', null=False, blank=False)
    system_restriction = models.CharField(max_length=1, db_column='restricao_sistema', verbose_name='Restrição Sistema', choices=ATIVO_INATIVO, null=False, blank=False)
    project_type = models.CharField(max_length=255, db_column='projeto_tipo', verbose_name='Tipo do Projeto', null=False, blank=False)
    project_url_git = models.TextField(max_length=255, db_column='projeto_url_git', verbose_name='URL Git')
    project_name = models.CharField(max_length=255, db_column='projeto_nome', verbose_name='Projeto Nome')
    project_version = models.CharField(max_length=255, db_column='projeto_versao', verbose_name='Versão do projeto', null=False, blank=False)
    project_file_start = models.CharField(max_length=255, db_column='projeto_arquivo_start', verbose_name='Arquivo Start', null=False, blank=False)
    fluid_type = models.CharField(max_length=255, db_column='fluid_tipo', verbose_name='Fluid Tipo', null=True, blank=True)
    fluid_location = models.CharField(max_length=255, db_column='fluid_local', verbose_name='Fluid Local', null=True, blank=True)
    schema = models.CharField(max_length=255, db_column='table_name_schema', verbose_name='Schema', null=False, blank=False)
    table_name = models.CharField(max_length=255, db_column='table_name', verbose_name='Nome Tabela', null=False, blank=False)
    by_pass = models.CharField(max_length=255, db_column='by_pass', verbose_name='By Pass', null=False, blank=False, choices=ATIVO_INATIVO)
    
    
    class Meta:
        managed = False
        db_table = '"sustentacao"."automacao_new"'
        verbose_name = 'Automação'
        verbose_name_plural = "Automações"

    def __str__(self):
        return self.project_name
    

class TarefaNew(models.Model):
    id = models.IntegerField(primary_key=True)
    automation = models.ForeignKey(AutomacaoNew, on_delete=models.PROTECT, db_column='id_automacao', verbose_name='Automação')
    pending_routines = models.IntegerField(db_column='rotinas_pendentes', verbose_name='Rotina Pendente')
    processing_routines = models.IntegerField(db_column='rotinas_processando', verbose_name='Rotina Processando')
    errors_routines = models.IntegerField(db_column='rotinas_erros', verbose_name='Rotina Erro')
    total_routines = models.IntegerField(db_column='rotinas', verbose_name='Rotina Total')
    # Outros campos relevantes da tabela tarefa_new
    
    class Meta:
        managed = False
        db_table = '"sustentacao"."tarefa_new"'
        verbose_name = 'Tarefa'
        verbose_name_plural = "Tarefas"
        ordering = ['automation__priority', 'processing_routines', 'pending_routines', 'errors_routines']

    def __str__(self):
        return str(self.id)


class RoboNew(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name='ID')
    description = models.CharField(max_length=255, verbose_name='Nome', db_column='nome')
    automation = models.ForeignKey(AutomacaoNew, on_delete=models.PROTECT, db_column='id_automacao', verbose_name='Automação', blank=True, null=True)
    situation = models.ForeignKey(SituacaoRobo, on_delete=models.PROTECT, db_column='id_situacao', verbose_name='Situação')
    type = models.CharField(max_length=255, db_column='tipo', verbose_name='Tipo do robô')
    host_name = models.CharField(max_length=255, db_column='host_name', verbose_name='Nome da máquina')
    host_ip = models.CharField(max_length=255, db_column='host_ip', verbose_name='IP da máquina')
    priority = models.CharField(max_length=1, db_column='prioritario', choices=ATIVO_INATIVO, verbose_name='Prioritário')
    active = models.CharField(max_length=1, db_column='ativo', verbose_name='Ativo', choices=ATIVO_INATIVO)
    
    class Meta:
        managed = False
        db_table = '"sustentacao"."robo_new"'
        verbose_name = 'Robô'
        verbose_name_plural = "Robôs"
        ordering = ['automation', 'description']

    def __str__(self):
        return self.description
        
        
class RoboHasAutomacao(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name='ID')
    robot = models.ForeignKey(RoboNew, on_delete=models.PROTECT, db_column='id_robo', verbose_name='Robo')
    automation = models.ForeignKey(AutomacaoNew(), on_delete=models.PROTECT, db_column='id_automacao', verbose_name='Automação')

    class Meta:
        managed = False
        db_table = '"sustentacao"."robo_has_automacao"'
        verbose_name = 'Robo - Automação'
        verbose_name_plural = "Robos - Automações"
        ordering = ['robot']

    def __str__(self):
        return f'{self.robot.descricao} - {self.automation.project_name}'
        

class HistoricoTabela(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name='ID')
    affected_table = models.TextField(verbose_name='Tabela Afetada', db_column='tabela_afetada')
    action = models.TextField(verbose_name='Ação', db_column='acao')
    data = models.JSONField(verbose_name='Dados', db_column='dados')
    date_hour = models.DateTimeField(verbose_name='Data e Hora do registro', db_column='data_hora')

    class Meta:
        managed = False
        db_table = '"rastreabilidade"."historico_tabela"'
        verbose_name = 'Histórico Tabela'
        


