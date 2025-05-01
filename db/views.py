# meu_app/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services.rotinas import listar_todos_os_erros, alterar_situacao_rotina

def listar_erros_view(request):
    erros = listar_todos_os_erros()
    return JsonResponse({'erros': erros}, safe=False)

@csrf_exempt
def corrigir_erro_view(request, schema, tabela, id_rotina):
    if request.method == 'POST':
        alterar_situacao_rotina(schema, tabela, id_rotina, '1')
        return JsonResponse({'status': 'sucesso', 'mensagem': 'Erro corrigido para 1'})
    else:
        return JsonResponse({'status': 'erro', 'mensagem': 'Método não permitido'}, status=405)
