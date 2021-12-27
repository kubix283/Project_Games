from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView  # new
from .models import Game


class GameListView(LoginRequiredMixin, ListView):
    model = Game
    context_object_name = 'game_list'
    template_name = 'games/game_list.html'
    login_url = 'account_login'


class GameDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Game
    context_object_name = 'game'
    template_name = 'games/game_detail.html'
    login_url = 'account_login'
    permission_required = 'games.special_status'
