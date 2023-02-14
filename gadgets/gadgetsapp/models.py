from django.db import models

# Create your models here.
class Gadgets(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    brand = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
