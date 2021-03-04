from django.db import models

class messages(models.Model):
    name = models.TextField(max_length=30)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    def __str__(self):
        return self.name


class contact(models.Model):
    name = models.TextField(max_length=30)
    email = models.EmailField()
    message = models.CharField(max_length=10)
