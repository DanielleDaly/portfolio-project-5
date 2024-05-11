import uuid

from django.db import models

from django_countries.fields import CountryField


class CustomerEnquiry(models.Model):

    class Meta:
        verbose_name_plural = 'Customer Enquiries'

    enquiry_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    enquiry = models.TextField(null=False, blank=False, default='')
    country = CountryField(blank_label='Country *', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def _generate_enquiry_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the enquiry number
        """
        if not self.enquiry_number:
            self.enquiry_number = self._generate_enquiry_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.enquiry_number
