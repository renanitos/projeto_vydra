from django import forms

class BuscaFuncionario(forms.Form):
    nome = forms.CharField(label='Nome do funcionário', max_length=100)


