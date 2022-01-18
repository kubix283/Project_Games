from django import forms

from games.models import Game


class NewGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'author', 'type', 'platforms', 'producents', 'publishers', 'price', 'cover']
