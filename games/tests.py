from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from .models import Review, Game


class BookTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@example.com',
            password='testpass123'
        )
        self.special_permissions = Permission.objects.get(codename='special_status')

        self.game = Game.objects.create(
            name='Harry Potter',
            author='JK Rowling',
            price='25.00',
        )

        self.review = Review.objects.create(
            game=self.game,
            author=self.user,
            review='An example review',
        )

    def test_game_listing(self):
        self.assertEqual(f'{self.game.name}', 'Harry Potter')
        self.assertEqual(f'{self.game.author}', 'JK Rowling')
        self.assertEqual(f'{self.game.price}', '25.00')


    def test_game_list_for_logged_in_user(self):
        self.client.login(email='reviewuser@example.com', password='testpass123')
        response = self.client.get(reverse('game_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'games/game_list.html')

    def test_game_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('game_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '%s?next=/games/' % (reverse('account_login')))
        response = self.client.get('%s?next=/games/' % (reverse('account_login')))
        self.assertContains(response, 'Log In')

    def test_game_detail_view_with_permissions(self):
        self.client.login(email='reviewuser@example.com', password='testpass123')
        self.user.user_permissions.add(self.special_permissions)
        response = self.client.get(self.game.get_absolute_url())
        no_response = self.client.get('/games/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'An example review')
        self.assertTemplateUsed(response, 'games/game_detail.html')
