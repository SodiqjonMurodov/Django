from django.db import models

class Main(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=500)
    age = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name