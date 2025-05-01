from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = "Categorias"
        ordering = ['name']


class ErrorCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    Category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='error_categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Erro Categorizado'
        verbose_name_plural = "Erros Categorizados"
        ordering = ['name']