# meu_app/services/rotinas.py

from django.db import connection
from ..models import AutomacaoNew

def buscar_erros_tabela(schema_name, tabela_rotina):
    with connection.cursor() as cursor:
        cursor.execute(f'''
            SELECT id, id_robo, id_situacao, obs
            FROM {schema_name}.{tabela_rotina}
            WHERE id_situacao = '3'
        ''')
        colunas = [col[0] for col in cursor.description]
        resultados = [
            dict(zip(colunas, linha))
            for linha in cursor.fetchall()
        ]
    return resultados

def listar_todos_os_erros():
    erros = []
    automacoes = AutomacaoNew.objects.all()
    for automacao in automacoes:
        erros_atuais = buscar_erros_tabela(
            automacao.schema,
            automacao.tabela_rotina
        )
        for erro in erros_atuais:
            erro['tabela_rotina'] = automacao.tabela_rotina
            erro['schema'] = automacao.schema
            erros.append(erro)
    return erros

def alterar_situacao_rotina(schema_name, tabela_rotina, id_rotina, nova_situacao):
    with connection.cursor() as cursor:
        cursor.execute(f'''
            UPDATE {schema_name}.{tabela_rotina}
            SET id_situacao = %s
            WHERE id = %s
        ''', [nova_situacao, id_rotina])
