import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Game(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    TYPE_OF_GAMES = [
        ('UDF', 'Undefined'),
        ('AC', 'Action'),
        ('AC-ADV', 'Action-adventure'),
        ('ADV', ' Adventure'),
        ('RP', 'Role-playing'),
        ('SM', 'Simulation'),
        ('STR', 'Strategy'),
        ('SPO', 'Sports'),
        ('MMO', 'MMO'),
        ('SB', 'Sandbox')
    ]
    PLATFORMS = [
        ('Windows', 'Windows'),
        ('Android', 'Android'),
        ('Xbox', 'Xbox'),
        ('PS', 'Playstation'),
        ('Nintendo', 'Nintendo')
    ]
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    type = models.CharField(max_length=6, choices=TYPE_OF_GAMES, default='UDF')
    platforms = models.CharField(max_length=8, choices=PLATFORMS, default='Windows')
    producents = models.CharField(max_length=64)
    publishers = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game_detail', args=[str(self.id)])

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.review