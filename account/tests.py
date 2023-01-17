
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from account.forms import AuthenticationForm

User = get_user_model()

class TestRegisterUser(TestCase):
    ''' Тестирование views ригистрации пользователей '''
    def test_get(self):
        ''' Получение формы регистрации '''
        response = self.client.get(reverse('register'))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], AuthenticationForm)

    def test_post_error(self):
        ''' Тестирование регистрацип пользователя с ошибками '''
        payload = {
            'username': 'username',
            'email': 'drinks@gmail.com',
            'password1': 'Pass12345',
            'password2': '12345',
        }

        response = self.client.post(reverse('register'), data=payload)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], AuthenticationForm)
        self.assertIn('password2', response.context['form'].errors)

    def test_post_ok(self):
        ''' Тестирование регистрацип пользователя '''
        email = 'drinks@gmail.com'
        payload = {
            'username': 'username',
            'email': email,
            'password1': 'Pass12345',
            'password2': 'Pass12345',
        }

        response = self.client.post(reverse('register'), data=payload)
        user = User.objects.get(email=email)

        self.assertEqual(user.email, email)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(user.is_authenticated)