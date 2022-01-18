from django.urls import path
from .views import GameListView, GameDetailView, SearchResultListView, game_create

urlpatterns = [
    path('', GameListView.as_view(), name='game_list'),
    path('<uuid:pk>/', GameDetailView.as_view(), name='game_detail'),
    path('search/', SearchResultListView.as_view(), name='search'),
    path('AddGame/', game_create, name='add_game'),
]
