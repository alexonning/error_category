# admin.py
from django.contrib import admin
from django.db import connection
from .models import Category, ErrorCategory


@admin.register(ErrorCategory)
class ErrorCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'listar_registros_rotinas')

    def listar_registros_rotinas(self, obj):
        tabelas = self.listar_tabelas_com_id_situacao()
        resultados = []

        for tabela in tabelas:
            registros = self.buscar_registros_situacao_3(tabela)
            if registros:
                resultados.append(f"Tabela {tabela}: {len(registros)} registros")

        return "; ".join(resultados) if resultados else "Nenhum registro"

    listar_registros_rotinas.short_description = "Registros nas Rotinas (id_situacao=3)"

    def listar_tabelas_com_id_situacao(self):
        """
        Lista todas as tabelas no schema 'rotinas' que possuem a coluna 'id_situacao'.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT table_name
                FROM information_schema.columns
                WHERE table_schema = 'rotina'
                  AND column_name = 'id_situacao';
            """)
            tabelas = [row[0] for row in cursor.fetchall()]
        return tabelas

    def buscar_registros_situacao_3(self, tabela):
        """
        Busca registros da tabela especificada com id_situacao = 3.
        """
        with connection.cursor() as cursor:
            try:
                cursor.execute(f'''
                    SELECT * FROM "rotina"."{tabela}"
                    WHERE id_situacao = 3;
                ''')
                rows = cursor.fetchall()
                return rows
            except Exception as e:
                # Caso dê erro na tabela (por exemplo: não tenha id_situacao ou permissões)
                return []

admin.site.register(Category)