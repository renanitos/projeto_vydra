from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from login.models import Funcionarios, FuncionarioUsuario
from login.forms import BuscaFuncionario
from django.contrib import messages

# PAGINA INICIAL
def index(request):
    return render(request, 'index.html')

# LOGIN DO USUARIO
# PAGINA DE LOGIN
def login_page(request):
    return render(request, 'login_page.html')
# PROCESSAMENTO DO LOGIN
def processa_login(request):
    dados = {}
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('dashboard')
    else:
        dados['msg'] = 'Usuário ou senha inválidos!'
        dados['class'] = 'alert-danger'
        return render(request, 'login_page.html', dados)

# PAGINAS DO USUARIO
def dashboard(request):
    return render(request, 'dashboard.html')
#OKR
def okr(request):
    return render(request, 'okr.html')
#ORGANOGRAMA
def organograma(request):
    return render(request, 'organograma.html')

#PAINEL DE CONTROLE DO SISTEMA
# TODOS OS FUNCIONARIOS
def lista_de_funcionarios(request):
    todos_funcionarios = Funcionarios.objects.all()
    return render(request, 'lista_de_funcionarios.html', {'todos_funcionarios' : todos_funcionarios})
#LISTAGEM DE FUNCIONARIOS
def lista_de_usuarios(request):
    usuario = User.objects.all()
    return render(request, 'perfil.html', {'usuario' : usuario})


#PÁGINA DE CRIAÇÃO DE FUNCIONARIO
def criar_funcionario(request):
    return render(request, 'criar_funcionario.html')

#CRIA NOVO FUNCIONARIO
def inserindo_funcionario(request):
    if request.method == "POST":
        #RECEBE DADOS DO FORMULÁRIO
        primeiro_nome = request.POST['primeiro_nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        data_nascimento = request.POST['data_nascimento']
        #data_admissao = request.POST['data_admissao']
        cpf = request.POST['cpf']
        salario = request.POST['salario']
        if primeiro_nome == '' or sobrenome == '' or email == '' or data_nascimento == '' or cpf == '' or salario == '':
            messages.error(request, 'Insira todos os dados no formulário!')
            return redirect('criar_funcionario')
        else:
            #CRIA UM NOVO FUNCIONÁRIO NO BANCO
            novo_funcionario = Funcionarios.objects.create(primeiro_nome=primeiro_nome,
            sobrenome=sobrenome, cpf=cpf, data_nascimento=data_nascimento,
            salario=salario, email=email)
            novo_funcionario.save()       
            #CRIA UM NOVO USER
            usuario = User.objects.create_user(username=email, email=email, password=cpf)
            #VINCULA USER COM FUNCIONARIO
            funcionario_usuario = FuncionarioUsuario(user=usuario, funcionarios=novo_funcionario)
            funcionario_usuario.save()
            #RETORNA MENSAGEM DE SUCESSO
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('criar_funcionario')
 
    return render(request, 'criar_funcionario.html')


#RESEARCH
def busca(request):
    form = BuscaFuncionario(request.GET)
    funcionarios = []
    if form.is_valid():
        nome = form.cleaned_data['primeiro_nome']
        funcionarios = Funcionarios.objects.filter(nome__icontains=nome)
    return render(request, 'lista_de_funcionarios.html', {'form':form, 'funcionarios': funcionarios})

#UPDATE
#PAGINA DE ATUALIZAÇÃO
def atualizar_funcionario(request):
    return render(request, 'atualizar_funcionario.html')
# SELECIONA O USUARIO PELO ID PARA MODIFICAÇÃO
def modifica_funcionario(request, id):
    funcionario = Funcionarios.objects.get(id=id)
    return render(request, 'atualizar_funcionario.html', {'funcionario' : funcionario})
# ATUALIZA OS DADOS DO USUARIO NO BANCO
def processa_atualizacao_funcionario(request, id):
    funcionario = Funcionarios.objects.get(id=id)
    funcionario.primeiro_nome = request.POST['primeiro_nome']
    funcionario.sobrenome = request.POST['sobrenome']
    funcionario.email = request.POST['email']
    funcionario.data_nascimento = request.POST['data_nascimento']
    funcionario.data_admissao = request.POST['data_admissao']
    funcionario.cpf = request.POST['cpf']
    ativo = request.POST['ativo']
    if ativo == 'on':
        funcionario.ativo = True
    else:
        funcionario.ativo = False
    funcionario.salario = request.POST['salario']
    funcionario.save()
    return redirect(lista_de_funcionarios)

#DELETE
def deletar_funcionario(request, id):
    funcionario = Funcionarios.objects.get(id=id)
    funcionario.delete()
    return redirect(lista_de_funcionarios)



#PERFIL DO USUÁRIO
def perfil(request):
    usuario = request.user
    usuario_funcionario = FuncionarioUsuario.objects.get(user=usuario)
    funcionario = usuario_funcionario.funcionarios
    return render(request, 'perfil.html', {'funcionario': funcionario})
#MUDANÇA DE SENHA
#PÁGINA DE MUDANÇA DE SENHA
def mudar_senha(request):
    return render(request, 'mudar_senha.html')
# MUDAR A SENHA
def processa_senha(request):
    dados = {}
    senha = str(User.objects.get(password=request.user.password)) 
    if senha != request.POST['password']:
        dados['msg'] = 'Senha atual divergente!'
        dados['class'] = 'alert-danger'
        return render(request, 'mudar_senha.html', dados) 

    if (request.POST['new_password'] != request.POST['conf_new_password']):
        dados['msg'] = 'Senha e confirmação diferentes!'
        dados['class'] = 'alert-danger'
        return render(request, 'mudar_senha.html', dados)
    # SUCESSO
    if senha == request.POST['password'] and (request.POST['new_password'] == request.POST['conf_new_password']):
        user = User.objects.get(email=request.user.email)
        user.set_password(request.POST['new_password'])
        user.save()
        dados['msg'] = 'Senha alterada com sucesso! Refaça o Login.'
        dados['class'] = 'alert-success'
        return redirect(login_page)  

# LOGOUT DO SISTEMA
def sair(request):
    logout(request)
    return redirect('login_page')















