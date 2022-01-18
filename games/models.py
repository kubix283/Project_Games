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
        ('Undefined', 'Undefined'),
        ('Action', 'Action'),
        ('Action-adventure', 'Action-adventure'),
        ('Adventure', ' Adventure'),
        ('Role-playing', 'Role-playing'),
        ('Simulation', 'Simulation'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('MMO', 'MMO'),
        ('Sandbox', 'Sandbox')
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
    type = models.CharField(max_length=16, choices=TYPE_OF_GAMES, default='Undefined')
    platforms = models.CharField(max_length=8, choices=PLATFORMS, default='Windows')
    producents = models.CharField(max_length=64)
    publishers = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    class Meta:
        permissions = [
            ('special_status', 'Can play all games')
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game_detail', kwargs={'pk': str(self.pk)})

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.review

class Porada(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=264)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

