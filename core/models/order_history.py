from django.db import models
from django.contrib.auth.models import User
from .order import Order


class OrderHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_array = models.ManyToManyField(Order)

    def __str__(self):
        return self

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_order_history"
        app_label = "core"
