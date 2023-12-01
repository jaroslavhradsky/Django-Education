from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email
