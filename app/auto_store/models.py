from django.db import models

# Create your models here.


class Employee(models.Model):

    name = models.CharField(
        max_length=30,
        help_text='Employee Name',
        default='name'
    )

    age = models.PositiveSmallIntegerField(
        help_text='Vacation Days',
        default=50
    )

    USERNAME_FIELD = 'name'
