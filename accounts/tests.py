from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.forms import CustomUserRegisterForm
from model_bakery import baker

User = get_user_model()

class AccountsModelsTests(TestCase):

    def test_custom_user_creation(self):
        user = baker.make(User,age=25,bio="Test bio")
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.username)
        self.assertIsNotNone(user.age)
        self.assertIsNotNone(user.bio)

class AccountsFormsTests(TestCase):
    def test_registration_form_valid(self):
        data = {'username': 'testuser', 'password1': 'StrongPass123', 'password2': 'StrongPass123','email': 'test@example.com'}
        form = CustomUserRegisterForm(data)
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid(self):
        data = {'username': '', 'password1': '123', 'password2': '321'}
        form = CustomUserRegisterForm(data)
        self.assertFalse(form.is_valid())