from django.db import models
from django.contrib.auth.models import User
from course.models import Course

# Create your models here.
# The old Student model has been removed as it is replaced by Django's built-in User model.

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f'{self.user.username} enrolled in {self.course.name}'