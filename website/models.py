from django.db import models


# Create your models here.

class Formulario(models.Model):
    nome = models.CharField(max_length=30)
    apelido = models.CharField(max_length=35, default="")
    email = models.CharField(max_length=50)
    idade = models.IntegerField(default=1)
    data_nascimento = models.DateField(default="")

    def __str__(self):
        return self.email[:50]


class Quizz(models.Model):
    questao1 = models.CharField(max_length=100)
    questao2 = models.CharField(max_length=100)
    questao3 = models.CharField(max_length=100)
    questao4 = models.CharField(max_length=100)
    questao5 = models.CharField(max_length=100)
    questao6 = models.CharField(max_length=100)
    questao7 = models.CharField(max_length=100)
    questao8 = models.CharField(max_length=100)
    questao9 = models.CharField(max_length=100)
    questao10 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.questao1},{self.questao2},{self.questao3}, {self.questao4},{self.questao5},{self.questao6}" \
               f",{self.questao7},{self.questao8},{self.questao9},{self.questao10}"


class Comentario(models.Model):
    comentario = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.comentario}"

