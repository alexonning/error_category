# admin.py
from django.contrib import admin
from .models import Category, ErrorCategory
from import_export.admin import ImportExportModelAdmin
from django.db import connections
from django.contrib import messages
from .forms import ErrorCategoryForm


# Registro padrão para Category
# admin.site.register(Category)

# Customização do admin para ErrorCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Campos a serem exibidos
    list_display = ('id', 'name', 'description', 'requires_description')

    # Filtros
    list_filter = ['name', 'requires_description']



@admin.register(ErrorCategory)
class ErrorCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = ErrorCategoryForm
    
    # Campos a serem exibidos
    list_display = ('id', 'routine_id', 'affected_table', 'description_error', 'Category')

    # Campos somente leitura
    readonly_fields = ('routine_id', 'affected_table', 'description_error', 'date_hour', 'extra_data')
    
    # Filtros
    list_filter = ['Category', 'situation', 'affected_table', 'date_hour']

    # Campos de busca
    search_fields = ['description_error']
    
    
    fieldsets = (
            ('Informações Básicas', {
                'classes': ('tab-basic',),
                'fields': ('affected_table', 'description_error', 'robot', 'situation', 'Category', 'description')
            }),
            ('Detalhes Avançados', {
                'classes': ('tab-advanced',),
                'fields': ('routine_id', 'date_hour', 'extra_data')
            }),
        )
    
    def save_model(self, request, obj, form, change):
        # Captura os dados do formulário
        affected_table = obj.affected_table # Tabela afetada
        routine_id = obj.routine_id # ID da rotina
        situation = form.cleaned_data.get('situation').id # ID da situação


        # Se a situação for 1, faz o update na tabela
        if situation == 1 and affected_table:
            with connections['postgres'].cursor() as cursor:
                try:
                    cursor.execute(f"""
                        UPDATE rotina.{affected_table}
                        SET id_situacao = %s, id_robo = null, obs = null, inicio = null, fim = null
                        WHERE id = %s and id_situacao = 3
                    """, [situation, routine_id])
                except Exception as e:
                    self.message_user(request, f"Erro ao atualizar a tabela {affected_table}: {e}", level='error')

        # Salva normalmente o objeto
        super().save_model(request, obj, form, change)

