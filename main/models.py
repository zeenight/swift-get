# Create your models here.
import uuid  

from django.db import models
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=255)

    @property
    def is_expensive(self):
        return self.price > 1000000
