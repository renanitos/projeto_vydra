from django.contrib import admin
from django.urls import path
from login.views import index, atualizar_funcionario, busca, deletar_funcionario, perfil, processa_atualizacao_funcionario, okr, organograma, modifica_funcionario, lista_de_funcionarios , criar_funcionario, dashboard, login_page, processa_login, sair, mudar_senha, processa_senha, inserindo_funcionario

urlpatterns = [
    #ADMIN
    path('admin/', admin.site.urls),

    #PÁGINA INICIAL
    path('', login_page, name='home'),

    #LOGIN DO USUÁRIO
    path('login_page', login_page, name='login_page'),
    path('processa_login', processa_login, name='processa_login'),
    
    #PÁGINAS DO USUÁRIO
    path('dashboard', dashboard, name='dashboard'),
    path('okr', okr, name='okr'),
    path('organograma', organograma, name='organograma'),

    #PAINEL DE CONTROLE DO SISTEMA
    path('lista_de_funcionarios', lista_de_funcionarios, name='lista_de_funcionarios'),

    #CRUD USUARIO/FUNCIONARIO
    #CREATE
    path('criar_funcionario', criar_funcionario, name='criar_funcionario'),
    path('inserindo_funcionario', inserindo_funcionario, name='inserindo_funcionario'),

    #RESEARCH
    path('busca', busca, name='busca'),

    #UPDATE
    path('atualizar_funcionario', atualizar_funcionario, name='atualizar_funcionario'),
    path('modifica_funcionario/<int:id>', modifica_funcionario, name='modifica_funcionario'),
    path('processa_atualizacao_funcionario/<int:id>', processa_atualizacao_funcionario, name='processa_atualizacao_funcionario'),

    #DELETE
    path('deletar_funcionario/<int:id>', deletar_funcionario, name='deletar_funcionario'),

    #PERFIL
    path('perfil', perfil, name='perfil'),
    path('mudar_senha', mudar_senha, name='mudar_senha'),
    path('processa_senha', processa_senha, name='processa_senha'),
    path('sair', sair, name='sair'),

    ]
