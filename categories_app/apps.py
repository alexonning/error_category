from django.apps import AppConfig


class CategoriesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'categories_app'  # Certifique-se de que o nome corresponde ao diretório do app
    verbose_name = 'Categorias'