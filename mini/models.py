from django.db import models

# Create your models here.

class Birthday(models.Model):
    Name = models.CharField(max_length=25)
    Date = models.CharField(max_length=20)
    Greeting = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return f'{self.name}'
