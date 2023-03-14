from django.db import models
from django.shortcuts import reverse

CHOICES = (

    ('1', 'Full name'),
    ('2', 'Job'),
    ('3', 'Email'),
    ('4', 'Domain name'),
    ('5', 'Phone number'),
    ('6', 'Company name'),
    ('7', 'Text'),
    ('8', 'Integer'),
    ('9', 'Address'),
    ('10', 'Date')

    )


class Schema(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Name -  {self.name} ID - {self.pk}"

    def get_detail_url(self, *args, **kwargs):
        return reverse('schema_detail', kwargs={'pk': self.pk})

    def get_update_url(self, *args, **kwargs):
        return reverse('schema_update', kwargs={'pk': self.pk})

    def get_delete_url(self, *args, **kwargs):
        return reverse('schema_delete', kwargs={'pk': self.pk})


class Data(models.Model):
    data_name = models.CharField(max_length=30, verbose_name="Column name")
    data_type = models.CharField(max_length=30, choices=CHOICES, default="Choose...", verbose_name="Type")
    order = models.IntegerField(default="0")
    created_at = models.DateTimeField()

    def __str__(self):
        return f"ID -  {self.data_name} "


