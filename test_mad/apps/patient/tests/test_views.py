from rest_framework.test import APIClient
from rest_framework import status
from apps.patient.models import Patient
from apps.user.models import User
import pytest

@pytest.mark.django_db
class TestPatientEndpoints:
    def setup_method(self):
        self.client = APIClient()
        self.patients_url = '/api/patients/'
        self.doctor = User.objects.create_user(email="TestUser5@gmail.com", password="TestUserTestUser123", is_doctor=True)
        self.patient = Patient.objects.create(first_name="John", last_name="Doe", diagnoses=["Diagnosis 1", "Diagnosis 2"])

    def test_get_patients_as_doctor(self):
        self.client.force_authenticate(user=self.doctor)
        response = self.client.get(self.patients_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_get_patients_as_non_doctor(self):
        non_doctor = User.objects.create_user(email="TestUser7@gmail.com", password="TestUserTestUser123", is_doctor=False)
        self.client.force_authenticate(user=non_doctor)
        response = self.client.get(self.patients_url)
        assert response.status_code == status.HTTP_403_FORBIDDEN
