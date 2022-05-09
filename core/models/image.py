from django.db import models
import core.models as core

class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    default = models.BooleanField(default=False)

class ItemImages(models.Model):
    item = models.ForeignKey(core.Item, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image)
