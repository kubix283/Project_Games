from django.contrib import admin
from games.models import Game, Review, Porada


class ReviewInline(admin.TabularInline):
    model = Review


class GameAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ['name', 'author', 'type', 'platforms', 'price']

class PoradaAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']



admin.site.register(Game, GameAdmin)
admin.site.register(Porada, PoradaAdmin)

