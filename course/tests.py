from django.test import TestCase
from django.urls import reverse
from .models import Course

class CourseViewsTestCase(TestCase):
    def setUp(self):
        self.course1 = Course.objects.create(name='Math', description='Basic Math', fee=100)
        self.course2 = Course.objects.create(name='Science', description='Basic Science', fee=150)

    def test_course_list_view_status_code(self):
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200)

    def test_course_list_view_uses_correct_template(self):
        response = self.client.get(reverse('course_list'))
        self.assertTemplateUsed(response, 'course/course_list.html')

    def test_course_list_view_displays_courses(self):
        response = self.client.get(reverse('course_list'))
        self.assertContains(response, self.course1.name)
        self.assertContains(response, self.course2.name)

    def test_course_detail_view_status_code(self):
        response = self.client.get(reverse('course_detail', args=[self.course1.id]))
        self.assertEqual(response.status_code, 200)

    def test_course_detail_view_uses_correct_template(self):
        response = self.client.get(reverse('course_detail', args=[self.course1.id]))
        self.assertTemplateUsed(response, 'course/course_detail.html')

    def test_course_detail_view_displays_correct_course(self):
        response = self.client.get(reverse('course_detail', args=[self.course1.id]))
        self.assertContains(response, self.course1.name)
        self.assertContains(response, self.course1.description)
        self.assertContains(response, str(self.course1.fee))
