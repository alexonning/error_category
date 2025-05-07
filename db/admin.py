# admin.py
from django.contrib import admin
from django.db.models import Q
from .models import AutomacaoNew, TarefaNew, RoboNew

@admin.register(AutomacaoNew)
class AutomacaoNewAdmin(admin.ModelAdmin):
    # Campos a serem exibidos
    list_display = ('project_name', 'schema', 'table_name', 'project_version', 'priority')

    # # Campos somente leitura
    readonly_fields = ['id']

    fieldsets = (
            ('Informações Principais', {
                'classes': ('tab-basic',),
                'fields': ('id', 'situation', 'schema', 'table_name', 'project_name', 'system_restriction', 'project_version', 'priority', 'limit_attempts', 'project_type', 'by_pass', 'project_url_git')
            }),
            ('Detalhes Fluid', {
                'classes': ('tab-advanced',),
                'fields': ('fluid_type', 'fluid_location', 'action_protocol', 'action_return')
            }),
            ('Detalhes Calculo', {
                'classes': ('tab-advanced',),
                'fields': ('quick_task_calculation', 'average_executor_time', 'median_executor_time', 'executor_time', 'maximum_average_execution_time', 'average_execution_time', 'sla_execution', 'sla_wait', 'robot_cost')
            }),
            ('Detalhes Avançados', {
                'classes': ('tab-advanced',),
                'fields': ('project', 'task_unique', 'indeed', 'description', 'project_file_start', 'business_day_only', 'robot_limits')
            }),
        )


@admin.register(TarefaNew)
class TarefaNewAdmin(admin.ModelAdmin):
    # Campos a serem exibidos
    list_display = ('id', 'automation', 'automation__priority', 'total_routines', 'pending_routines', 'processing_routines', 'errors_routines')

    readonly_fields = ['id']

    list_filter = ['automation', 'automation__priority', 'total_routines', 'pending_routines', 'processing_routines', 'errors_routines']

    # def changelist_view(self, request, extra_context=None):
    #     request.GET = request.GET.copy()
    #     if not any(key in request.GET for key in ['pending_routines__gt', 'processing_routines__gt', 'errors_routines__gt']):
    #         request.GET['pending_routines__gt'] = '0'
    #         request.GET['processing_routines__gt'] = '0'
    #         request.GET['errors_routines__gt'] = '0'
    #     return super().changelist_view(request, extra_context=extra_context)
    
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)

        try:
            cl = response.context_data['cl']
            queryset = cl.queryset
            filtered_queryset = queryset.filter(
                Q(pending_routines__gt=0) |
                Q(processing_routines__gt=0) |
                Q(errors_routines__gt=0)
            )
            cl.queryset = filtered_queryset
        except (AttributeError, KeyError):
            pass

        return response
    

    
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(Q(pending_routines__gt=0) | Q(processing_routines__gt=0) | Q(errors_routines__gt=0))


@admin.register(RoboNew)
class RoboNewAdmin(admin.ModelAdmin):
    # Campos a serem exibidos
    list_display = ('id', 'description', 'situation', 'automation', 'active', 'priority')
    
    # Campos somente leitura
    readonly_fields = ['id']
    
    # Filtros
    list_filter = ['description', 'situation', 'automation', 'active']

    fieldsets = (
            ('Informações Básicas', {
                'classes': ('tab-basic',),
                'fields': ('id', 'description', 'situation', 'automation', 'active')
            }),
            ('Detalhes Avançados', {
                'classes': ('tab-advanced',),
                'fields': ('type', 'host_name', 'host_ip', 'priority')
            }),
        )
    
    def save_model(self, request, obj, form, change):
        situation = form.cleaned_data.get('situation').id # ID da situação
        
        if situation == 1:
           obj.automation = None

        super().save_model(request, obj, form, change)