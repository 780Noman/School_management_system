from django.test import TestCase
from django.urls import reverse
from .models import Fee
from course.models import Course
from datetime import date

class FeesViewsTestCase(TestCase):
    def setUp(self):
        self.course1 = Course.objects.create(name='Math', description='Basic Math', fee=100)
        self.course2 = Course.objects.create(name='Science', description='Basic Science', fee=150)
        self.fee1 = Fee.objects.create(course=self.course1, amount=100, payment_date=date.today())
        self.fee2 = Fee.objects.create(course=self.course2, amount=150, payment_date=date.today())

    def test_fee_list_view_status_code(self):
        response = self.client.get(reverse('fees:fee_list'))
        self.assertEqual(response.status_code, 200)

    def test_fee_list_view_uses_correct_template(self):
        response = self.client.get(reverse('fees:fee_list'))
        self.assertTemplateUsed(response, 'fees/fee_list.html')

    def test_fee_list_view_displays_fees(self):
        response = self.client.get(reverse('fees:fee_list'))
        self.assertContains(response, self.fee1.course.name)
        self.assertContains(response, str(self.fee1.amount))
        self.assertContains(response, self.fee2.course.name)
        self.assertContains(response, str(self.fee2.amount))
