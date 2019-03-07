from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CustomUsers(User):
    """Basic model of users."""

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    created = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=2,
                              choices=GENDER_CHOICES, default=MALE)
    class Meta:
        # Sorted by name field
        ordering = ('username',)
