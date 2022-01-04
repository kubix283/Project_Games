from django.urls import path
from .views import ForumHomeView, ForumPoradyView, PoradyDodajView

urlpatterns = [
    path('', ForumHomeView.as_view(), name='forum_home'),
    path('porady/', ForumPoradyView.as_view(), name='forum_porady'),
    path('porady/dodaj', PoradyDodajView.as_view(), name='dodaj_porady')

]