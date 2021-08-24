from django.contrib import admin
from .models import Cliente, Barbearia, Servico, Ordem_Servico, Agenda
# from .models import QuillPost
# # Register your models here.

# @admin.register(QuillPost)
# class QuillPostAdmin(admin.ModelAdmin):
#     pass

class ClienteAdmin(admin.ModelAdmin):
    # fields = ('name', 'seconds') #limita a inserção de items no model
    list_display = ('id', 'name', 'surname', 'endereco', 'phone', 'email', 'cpf', 'created_at')  #coloca colunas na tabela de usuários no admin
    list_filter = ('id', 'name', 'surname', 'endereco', 'phone', 'email', 'cpf', 'created_at') #Cria um filtro na pesquisa
    search_fields = ('id', 'name', 'surname', 'endereco', 'phone', 'email', 'cpf', 'created_at')

class BarbeariaAdmin(admin.ModelAdmin):
    #fields = ('title', 'seconds') #limita a inserção de items no model
    list_display = ('id', 'name', 'phone', 'endereco', 'bio', 'email', 'document', 'date_closed', 'open_hour', 'closed_hour') #coloca colunas na tabela de usuários no admin
    list_filter = ('id', 'name', 'phone', 'endereco', 'email', 'document', 'date_closed', 'open_hour', 'closed_hour') #Cria um filtro na pesquisa
    search_fields = ('id', 'name', 'phone', 'endereco', 'email', 'document', 'date_closed', 'open_hour', 'closed_hour')

class ServicoAdmin(admin.ModelAdmin):
    #fields = ('title', 'seconds') #limita a inserção de items no model
    list_display = ('id', 'name', 'description', 'price', 'barbearia') #coloca colunas na tabela de usuários no admin
    list_filter = ('id', 'name', 'description', 'price', 'barbearia') #Cria um filtro na pesquisa
    search_fields = ('id', 'name', 'description', 'price', 'barbearia')

class OrdemServicoAdmin(admin.ModelAdmin):
    # fields = ('title', 'seconds') #limita a inserção de items no model
    list_display = ('id', 'barbearia', 'cliente', 'servico', 'created_at', 'avaliacao') #coloca colunas na tabela de usuários no admin
    list_filter = ('id', 'barbearia', 'cliente', 'servico', 'created_at', 'avaliacao') #Cria um filtro na pesquisa
    search_fields = ('id', 'barbearia', 'cliente', 'servico', 'created_at', 'avaliacao')

class AgendaAdmin(admin.ModelAdmin):
    # fields = ('title', 'seconds') #limita a inserção de items no model
    list_display = ('id', 'data', 'barbearia', 'servico', 'created_at', 'updated_at') #coloca colunas na tabela de usuários no admin
    list_filter = ('id', 'data', 'barbearia', 'servico', 'created_at', 'updated_at') #Cria um filtro na pesquisa
    search_fields = ('id', 'data', 'barbearia', 'servico', 'created_at', 'updated_at')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Barbearia, BarbeariaAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Ordem_Servico, OrdemServicoAdmin)
admin.site.register(Agenda, AgendaAdmin)