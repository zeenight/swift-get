# Create your models here.
import uuid
#TUGAS 4
from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=255)

    @property
    def is_expensive(self):
        return self.price > 1000000
