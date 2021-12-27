from django.urls import path
from .views import GameListView, GameDetailView, SearchResultListView

urlpatterns = [
    path('', GameListView.as_view(), name='game_list'),
    path('<uuid:pk>', GameDetailView.as_view(), name='game_detail'),
    path('search/', SearchResultListView.as_view(), name='search')
]
