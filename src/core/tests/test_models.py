from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import User


def create_user(user='teste', email='test_email@example.com') -> User:
    password = 'test123'
    firstname = 'Test'
    lastname = 'Last'
    user: User = get_user_model()

    return user.objects.create_user(
        username=user,
        password=password,
        email=email,
        first_name=firstname,
        last_name=lastname
    )


class TestModels(TestCase):
    def test_create_user_success(self):
        email = 'my_test@test.com'

        user = create_user(email=email)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password('test123'))
