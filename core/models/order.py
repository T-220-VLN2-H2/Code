from django.db import models
from django.utils.translation import gettext_lazy as _
import core.models as core
from django.contrib.auth.models import User


class Order(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    id = models.BigAutoField(primary_key=True)
    buyer = models.ForeignKey(
        User, related_name="buyer_users", on_delete=models.CASCADE
    )
    seller = models.ForeignKey(
        User, related_name="seller_users", on_delete=models.CASCADE
    )
    item = models.ForeignKey(core.Item, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(choices=RATING_CHOICES, null=True)

    def __str__(self):
        return self.id

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_order"
        app_label = "core"
