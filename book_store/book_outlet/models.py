from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Countries'

class Address(models.Model):
    street = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=5, null=True, blank=True)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.street}, {self.postal_code} {self.city}'
    
    class Meta:
        verbose_name_plural = 'Addresses'
    

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True) # One-to-one relation

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True) #One-to-many relation
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='', blank=True, null=False, db_index=True) # Harry Potter 1 -> harry-potter-1
    published_countries = models.ManyToManyField(Country) # Many-to-many relation

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse('book-detail', args=[self.id])
        return reverse('book-detail', args=[self.slug])

    def __str__(self) -> str:
        return f'{self.title} ({self.rating})'


