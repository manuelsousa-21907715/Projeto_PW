from django.shortcuts import render
from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
    path('', views.index_page_view, name='index'),
    path('about_Us', views.about_Us_page_view, name='about_Us'),
    path('produtos', views.produtos_page_view, name='produtos'),
    path('alimentos', views.alimentos_page_view, name='alimentos'),
    path('formulario', views.formulario_page_view, name='formulario'),
    path('galeria', views.galeria_page_view, name='galeria'),
    path('talho', views.talho_page_view, name='talho'),
    path('material', views.material_page_view, name='material'),
    path('form_django', views.form_django_page_view, name="form_django"),
    path('quizz', views.quizz_page_view, name="quizz"),
    path('resultado/<int:id>',views.resultado_page_view,name="resultado"),
    path('comentario', views.comentario_page_view, name='comentario'),
    path('add', views.add_page_view, name='add'),
    path('editar/<int:contact_id>', views.editar_page_view, name='editar'),
    path('apagar/<int:contact_id>', views.apagar_page_view, name='apagar'),
    path('single_page', views.javascript_page_view, name='single_page'),
]