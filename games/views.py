from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
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

class SearchResultListView(ListView):
    model = Game
    context_object_name = 'game_list'
    template_name = 'games/search_result_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Game.objects.filter(Q(name__icontains=query) | Q(author__icontains=query))