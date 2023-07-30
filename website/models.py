"""
creating database tables
"""
from django.db import models


# Create your models here.
class Record(models.Model):
    """creating database table called Records"""

    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
