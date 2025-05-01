# admin.py
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.db import connection
from .models import AutomacaoNew, TarefaNew, RoboNew

@admin.register(AutomacaoNew)
class AutomacaoNewAdmin(admin.ModelAdmin):
    list_display = ('projeto_nome', 'schema', 'nome_tabela')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('listar_todos_erros/', self.admin_site.admin_view(self.listar_todos_erros), name='listar_todos_erros'),
        ]
        return custom_urls + urls

    def listar_todos_erros(self, request):
        automacoes = AutomacaoNew.objects.using('postgres').all()
        todos_os_erros = []

        for automacao in automacoes:
            table_name = automacao.nome_tabela
            try:
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        SELECT
                            r.*,
                            rn.descricao AS nome_robo
                        FROM
                            "{automacao.schema}"."{table_name}" r
                        LEFT JOIN
                            public.robo_new rn ON r.robo_id = rn.id
                        WHERE
                            r.id_situacao = '3';
                    """)
                    colunas = [col[0] for col in cursor.description]
                    erros_desta_tabela = [dict(zip(colunas, row)) for row in cursor.fetchall()]
                    todos_os_erros.extend(erros_desta_tabela)
            except Exception as e:
                print(f"Erro ao consultar a tabela {automacao.schema}.{table_name}: {e}")

        context = {
            **self.admin_site.each_context(request),
            'title': 'Todos os Erros',
            'erros': todos_os_erros,
        }
        return render(request, 'admin/listar_todos_erros.html', context)

@admin.register(TarefaNew)
class TarefaNewAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_automacao')
    # ... outras configurações ...

@admin.register(RoboNew)
class RoboNewAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    # ... outras configurações ...