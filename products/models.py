from django.db import models

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

    def get_image(self):
        return self.image

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    isbn = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    author = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    external_url = models.CharField(max_length=254, null=True, blank=True)
    available_in_hardback = models.BooleanField(default=False, null=True, blank=True)
    num_pages = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name