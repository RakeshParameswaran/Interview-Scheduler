from datetime import date
from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

TIME_CHOICES = (
    ('9', '09:00 AM'),
    ('10', '10:00 AM'),
    ('11', '11:00 AM'),
    ('12', '12:00 PM'),
    ('13', '01:00 PM'),
    ('14', '02:00 PM'),
    ('15', '03:00 PM'),
    ('16', '04:00 PM'),
    ('17', '05:00 PM'),
    ('18', '06:00 PM'),
    ('19', '07:00 PM'),
)

class Student(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date = models.DateField(default = timezone.now())
    from_date = models.CharField(max_length = 2, choices = TIME_CHOICES, default = '9')
    to_date = models.CharField(max_length = 2, choices = TIME_CHOICES, default = '10')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
class Interviewer(models.Model):

    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    date = models.DateField(default = timezone.now())
    from_date = models.CharField(max_length = 2, choices = TIME_CHOICES, default = '9')
    to_date = models.CharField(max_length = 2, choices = TIME_CHOICES, default = '10')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)