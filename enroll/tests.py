from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import StudentReg

class EnrollViewsTestCase(TestCase):
    def test_registration_form_view_status_code(self):
        response = self.client.get(reverse('enroll'))
        self.assertEqual(response.status_code, 200)

    def test_registration_form_view_uses_correct_template(self):
        response = self.client.get(reverse('enroll'))
        self.assertTemplateUsed(response, 'enroll/userReg.html')

    def test_valid_registration_form_submission(self):
        self.assertEqual(User.objects.count(), 0)
        response = self.client.post(reverse('enroll'), {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password': 'password123',
            'password2': 'password123',
        })
        self.assertEqual(User.objects.count(), 1)
        self.assertRedirects(response, reverse('home'))

    def test_invalid_registration_form_submission(self):
        self.assertEqual(User.objects.count(), 0)
        response = self.client.post(reverse('enroll'), {
            'username': '',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password': 'password123',
            'password2': 'password123',
        })
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'enroll/userReg.html')
