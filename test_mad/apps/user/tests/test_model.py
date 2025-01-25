from apps.user.models import User
import pytest

@pytest.mark.django_db
class TestUserModel:
    def test_create_user(self):
        user = User.objects.create_user(email="TestUser4@gmail.com", password="TestUserTestUser123")
        assert user.email == "TestUser4@gmail.com"
        assert user.check_password("TestUserTestUser123") is True
        assert user.is_doctor is True

    def test_create_superuser(self):
        user = User.objects.create_superuser(email="admin5@gmail.com", password="TestUserTestUser123")
        assert user.is_staff is True
        assert user.is_superuser is True
