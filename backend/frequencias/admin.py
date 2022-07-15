from django.contrib import admin

# Register your models here.
from .models import FrequenciaAluno

class FrequenciaAlunoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'dia', 'entrada', 'saida')
    list_filter = ('dia',)
    search_fields = ['aluno__username']

admin.site.register(FrequenciaAluno, FrequenciaAlunoAdmin)
