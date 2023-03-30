from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Funcionarios(models.Model):
    primeiro_nome = models.CharField(max_length=30, null=False, blank=False)
    sobrenome = models.CharField(max_length=30, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    data_admissao = models.DateField(auto_now_add=True,null=False, blank=False)
    salario = models.FloatField(null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Nome: {self.primeiro_nome} | Sobrenome: {self.sobrenome} | Email: {self.email} | CPF: {self.cpf}"

class FuncionarioUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    funcionarios = models.OneToOneField(Funcionarios, on_delete=models.CASCADE)
