import uuid

from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Review(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False, default='')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title