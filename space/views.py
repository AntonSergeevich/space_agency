from django.shortcuts import render
from django.views.generic import ListView
from .models import IndexModel, SlideImg


class IndexView(ListView):
    model = IndexModel
    template_name = 'space/index.html'
    context_object_name = 'index'

    @staticmethod
    def index():
        title = 'Космическое агенство'
        desc = 'Национальное управление по аэронавтике и исследованию космического пространства - ведомство, относящееся' \
               'к федеральному правительству США и подчиняющееся непосредственно президенту США.'
        desc_img_1 = 'Спейс-шаттлы - пилотируемые корабли'
        desc_img_2 = 'Лучшее телескопическое оборудование'
        desc_img_3 = 'Целимся на Луну и Марс'
        desc_img_4 = 'Золотая медаль по научным исследованиям'
        index_all = [title, desc, desc_img_1, desc_img_2, desc_img_3, desc_img_4]

        return index_all

    @staticmethod
    def gallery():
        return SlideImg.objects.all()
