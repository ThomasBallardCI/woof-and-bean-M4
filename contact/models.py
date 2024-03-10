from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """ Model to set up Contact form """
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    content = models.CharField(max_length=2000, null=False, blank=False)
    date_submitted = models.DateTimeField(default=timezone.now,
                                          editable=False)

    class Meta:
        verbose_name = 'Contact Form'
        verbose_name_plural = 'Contact Forms'
        ordering = ['-date_submitted']
