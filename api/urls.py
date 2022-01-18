from django.urls import path
from .views import GameDetail, GameList

urlpatterns = [
    path('<uuid:pk>', GameDetail.as_view()),
    path('', GameList.as_view()),
]