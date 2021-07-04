from django.forms import ModelForm
from django import forms
from .models import Formulario
from .models import Quizz


class FormularioForm(ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'

class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'

        widgets = {
            'questao1': forms.TextInput(attrs={'placeholder': 'Responda Aqui', 'required': True}),
            'questao2': forms.TextInput(attrs={'placeholder': 'Responda Aqui', 'required': True}),
            'questao3': forms.TextInput(attrs={'placeholder': 'Responda Aqui', 'required': True}),
            'questao4': forms.TextInput(attrs={'placeholder': 'Responda Aqui', 'required': True}),
            'questao5': forms.TextInput(attrs={'placeholder': 'Responda Aqui', 'required': True}),
            'questao6': forms.TextInput(attrs={'placeholder': 'Responda Aqui', 'required': True}),
            'questao7': forms.TextInput(attrs={'placeholder': 'Responda Aqui', 'required': True}),
            'questao8': forms.TextInput(attrs={'placeholder': 'Responda Aqui', 'required': True}),
            'questao9': forms.TextInput(attrs={'placeholder': 'Responda Aqui', 'required': True}),
            'questao10': forms.TextInput(attrs={'placeholder': 'Responda Aqui', 'required': True}),
        }

        labels = {
            'questao1': '_____ ____ sabe bem pagar tão pouco:',
            'questao2': 'Tenho 10 euros, se pagar um produto de 5 euros com quanto fico?:',
            'questao3': 'Como se chama o supermercado que tem um elefante no logo:',
            'questao4': 'Tenho 20 euros, se pagar um produto de 10 euros com quanto fico?:',
            'questao5': 'Mini_____:',
            'questao6': 'Tenho 50 euros, se pagar um produto de 35 euros com quanto fico?:',
            'questao7': 'Supermercado com logo todo vermelho e começa com a letra "C"?:',
            'questao8': 'Tenho 500 euros, se pagar um produto de 480 euros com quanto fico?:',
            'questao9': 'Logo com background azul e uma roda amarela com 4 letras? :',
            'questao10': 'Tenho 200 euros, se pagar um produto de 175 euros com quanto fico?:',
        }

