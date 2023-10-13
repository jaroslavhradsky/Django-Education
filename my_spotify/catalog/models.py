from django.db import models

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=50, null=True)
    interpret = models.CharField(max_length=50, null=True)
    image = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return f'{self.name} by {self.interpret}'
