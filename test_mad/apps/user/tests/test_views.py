import pytest
from rest_framework.test import APIClient
from rest_framework import status
from apps.user.models import User


@pytest.mark.django_db
class TestUserRegistration:
    def setup_method(self):
        self.client = APIClient()
        self.register_url = '/api_auth/auth/users/'

    def test_register_user_success(self):
        data = {
            "email": "testuser@gmail.com",
            "password": "testuserTestUser123",
            "is_doctor": True
        }
        response = self.client.post(self.register_url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(email=data['email']).exists()

    def test_register_user_without_email(self):
        data = {
            "password": "testuserTestUser123",
            "is_doctor": True
        }
        response = self.client.post(self.register_url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_register_user_weak_password(self):
        data = {
            "email": "testuser2@gmail.com",
            "password": "123",
            "is_doctor": True
        }
        response = self.client.post(self.register_url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST




@pytest.mark.django_db
class TestTokenEndpoints:
    def setup_method(self):
        self.client = APIClient()
        self.token_url = '/api_auth/auth/jwt/create/'
        self.user = User.objects.create_user(
            email="testuser@gmail.com",
            password="testuserTestUser123"
        )

    def test_obtain_token_success(self):
        data = {
            "email": "testuser@gmail.com",
            "password": "testuserTestUser123"
        }
        response = self.client.post(self.token_url, data)
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
        assert 'refresh' in response.data

    def test_obtain_token_invalid_credentials(self):
        data = {
            "email": "testuser231@gmail.com",
            "password": "TesUserTestUser123"
        }
        response = self.client.post(self.token_url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

