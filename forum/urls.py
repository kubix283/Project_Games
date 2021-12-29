from django.urls import path
from .views import ForumHomeView, AboutMinecraftGameView

urlpatterns = [
    path('', ForumHomeView.as_view(), name='forum_home'),
    path('about/<uuid:pk>', AboutMinecraftGameView.as_view(), name='about_minecraft_game')
]