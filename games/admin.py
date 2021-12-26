from django.contrib import admin
from games.models import Game, Review


class ReviewInline(admin.TabularInline):
    model = Review

class GameAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ['name', 'author', 'type', 'platforms', 'price']


admin.site.register(Game, GameAdmin)
