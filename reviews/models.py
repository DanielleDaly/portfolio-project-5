import uuid

from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Review(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField(null=False, blank=False, default='')
    source = models.CharField(max_length=254, null=True, blank=True)
    source_url = models.CharField(max_length=254, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title