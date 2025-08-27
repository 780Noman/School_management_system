from django.db import models
from course.models import Course

class Fee(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='fees_set')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f'{self.course.name} - {self.amount}'