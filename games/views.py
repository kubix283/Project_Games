from django.views.generic import ListView, DetailView # new
from .models import Game


class GameListView(ListView):
    model = Game
    context_object_name = 'game_list'
    template_name = 'games/game_list.html'


class GameDetailView(DetailView):
    model = Game
    context_object_name = 'game'
    template_name = 'games/game_detail.html'
