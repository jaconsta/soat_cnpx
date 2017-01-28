from django.db import models


class Citizen(models.Model):
    """
    The insurance users.
    """

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    # Contact information
    email = models.EmailField()
    phone = models.CharField(max_length=50)

    # Citizen documents
    CC = 'CC'
    PASSPORT = 'PP'
    document_choices = (
        (CC, 'cc'),
        (PASSPORT, 'Passport')
    )
    document_type = models.CharField(max_length=5, choices=document_choices)
    document_number = models.BigIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
