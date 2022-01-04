from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView

from games.models import Game

from .forms import DodajPorade
from .models import ForumPorady


class ForumHomeView(ListView):
    model = Game
    context_object_name = 'game_list'
    template_name = 'forum/forum_home.html'


class ForumPoradyView(ListView):
    model = ForumPorady
    context_object_name = 'forum_porady_list'
    template_name = 'forum/porady/porady.html'

class PoradyDodajView(FormView):
    template_name = 'forum/porady/dodaj.html'
    form_class = DodajPorade
    success_url = '/forum/porady/'


