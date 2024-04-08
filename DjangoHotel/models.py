from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"Name: {self.name}, Rating: {self.rating}, Price: {self.price}"
