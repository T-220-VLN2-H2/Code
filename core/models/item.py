from django.db import models
from django.utils.translation import gettext_lazy as _
from .catagory import Catagory


# TODO: add display text


class Item(models.Model):
    class DeliveryType(models.TextChoices):
        # TODO: add text
        DELIVERY = "DELIVERY", _("Home delivery")
        PICKUP = "PICKUP", _("Self pickup")
        HANDOFF = "HANDOFF", _("???")

    class ConditionType(models.TextChoices):
        # TODO: add text
        NEW = "NEW", _("")
        USED = "USED", _("")
        USED_NEW = "USED_LIKE_NEW", _("")
        PARTS = "FOR_PARTS", _("For parts: not working")

    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    condition = models.CharField(choices=ConditionType.choices, max_length=128)
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    # TODO: add delivery options
    # delivery_Options = models.Array<DeliveryType>()

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_item"
        app_label = "core"
