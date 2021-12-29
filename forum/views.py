from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from games.models import Game


class ForumHomeView(ListView):
    model = Game
    context_object_name = 'game_list'
    template_name = 'forum/forum_home.html'

class AboutMinecraftGameView(DetailView):
    model = Game
    context_object_name = 'about_minecraft'
    template_name = 'forum/about_minecraft.html'
