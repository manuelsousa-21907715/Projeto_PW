from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
#import matplotlib.pyplot as plt
#from django_matplotlib import pyplot as plt
from website.forms import *

from .forms import FormularioForm
from .models import *



def quizz_page_view(request):
    resultados = QuizzForm(request.POST or None)
    if resultados.is_valid():
        idResultado = resultados.save()
        return HttpResponseRedirect('resultado/' + str(idResultado.id))

    context = {'resultados': resultados}

    return render(request, 'website/quizz.html', context=context)

def resultado_page_view(request, id):
    resultados = Quizz.objects.get(pk=id)
    nota = 0
    resultadoCorrecto = []

    if resultados.questao1.lower() != 'pingo doce':
        resultadoCorrecto.append(0)
    else:
        nota += 1
        resultadoCorrecto.append(1)

    if resultados.questao2 != '5':
        resultadoCorrecto.append(0)
    else:
        nota += 1
        resultadoCorrecto.append(1)

    if resultados.questao3.lower() != 'jumbo':

        resultadoCorrecto.append(0)
    else:
        nota += 1
        resultadoCorrecto.append(1)

    if resultados.questao4 != '10':

        resultadoCorrecto.append(0)
    else:
        nota += 1
        resultadoCorrecto.append(1)

    if resultados.questao5 != 'preço':

        resultadoCorrecto.append(0)
    else:
        nota += 1
        resultadoCorrecto.append(1)

    if resultados.questao6.lower() != '15':

        resultadoCorrecto.append(0)
    else:
        nota += 1
        resultadoCorrecto.append(1)

    if resultados.questao7.lower() != 'continente':

        resultadoCorrecto.append(0)
    else:
        nota += 1
        resultadoCorrecto.append(1)

    if resultados.questao8 != '20':

        resultadoCorrecto.append(0)
    else:
        nota += 1
        resultadoCorrecto.append(1)

    if resultados.questao9 != 'lidl':

        resultadoCorrecto.append(0)
    else:
        nota += 1
        resultadoCorrecto.append(1)

    if resultados.questao10 != '25':
        resultadoCorrecto.append(0)
    else:
        nota += 1
        resultadoCorrecto.append(1)

    #plt.style.use('fivethirtyeight')
    # dev_x = ["Certo", "Errado"]
    #dev_y = [nota, 10 - nota]
    #plt.bar(dev_x, dev_y)
    # plt.savefig('website/static/website/img/resultado.png')

    context = {
        '1': nota,
        #'2': plt,
        '3': resultados
    }

    return render(request, 'website/resultado.html', context)

def comentario():
    com_get = Comentario.objects.all()
    comentario = [0,0,0]

    for i in com_get:
        if i.comentario == "1":
            comentario[0] +=1
        elif i.comentario == "2":
            comentario[1] += 1
        elif i.comentario == "3":
            comentario[2] +=1

        # plt.title("Comentário geral do Website")
        # plt.xlabel('Qualidade do comentário sobre o site')
        # plt.ylabel('Número total de comentários')
        # plt.bar(["Não Satisfaz", "Médio", "Bom"], comentario)
        # plt.savefig('website/static/website/img/comentario.png')

def comentario_page_view(request):

    comentario()
    context = {
        # 'img': plt
    }
    #plt.close()

    if request.method == 'POST':
        if request.POST.get('avaliacao', "0"):
            comment = Comentario()
            comment.comentario = request.POST.get('comentario', "0")
            comment.save()
            comentario()
            context = {
                #   'img': plt
            }
            #plt.close()

            return render(request, 'website/comentario.html', context=context)
    else:
        return render(request, 'website/comentario.html', context=context)

def form_django_page_view(request):
    context = {'website': Formulario.objects.all()}
    return render(request, 'website/form_django.html', context)


def add_page_view(request):
    form = FormularioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:form_django'))

    context = {'form': form}

    return render(request, 'website/add.html', context)


def editar_page_view(request, contact_id):
    contacto = Formulario.objects.get(id=contact_id)

    form = FormularioForm(request.POST or None, instance=contacto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:form_django'))

    context = {'form': form, 'contact_id': contact_id}

    return render(request, 'website/editar.html', context)


def apagar_page_view(request, contact_id):
    Formulario.objects.get(id=contact_id).delete()
    return HttpResponseRedirect(reverse('website:form_django'))


def index_page_view(request):
    return render(request, 'website/index.html')


def about_Us_page_view(request):
    return render(request, 'website/about_Us.html')


def produtos_page_view(request):
    return render(request, 'website/produtos.html')


def material_page_view(request):
    return render(request, 'website/material.html')


def alimentos_page_view(request):
    return render(request, 'website/alimentos.html')


def talho_page_view(request):
    return render(request, 'website/talho.html')


def formulario_page_view(request):
    return render(request, 'website/formulario.html')


def galeria_page_view(request):
    return render(request, 'website/galeria.html')

def javascript_page_view(request):
    return render(request, 'website/single_page.html')