from django.db import models
from django.utils.translation import gettext_lazy as _
import core.models as core


class Item(models.Model):
    class DeliveryType(models.TextChoices):
        DELIVERY = "DELIVERY", _("Home delivery")
        PICKUP = "PICKUP", _("Self pickup")
        HANDOFF = "HANDOFF", _("Inperson handoff")

    class ConditionType(models.TextChoices):
        NEW = "NEW", _(
            "A brand-new, unused, unopened, undamaged item in its original packaging."
        )
        USED = "USED", _("An item that has been used previously.")
        USED_NEW = "USED_LIKE_NEW", _("Seller referbished.")
        PARTS = "FOR_PARTS", _(
            "An item that does not function as intended and is not fully operational. "
        )

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128, default="Item")
    price = models.DecimalField(decimal_places=2, max_digits=10)
    condition = models.CharField(choices=ConditionType.choices, max_length=128)
<<<<<<< HEAD
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    delivery_Option = models.CharField(choices=DeliveryType.choices, max_length=128)
=======
    category = models.ForeignKey(core.Category, on_delete=models.CASCADE)
    delivery_Option = models.CharField(
        choices=DeliveryType.choices, max_length=128, default=DeliveryType.PICKUP
    )
    description = models.TextField(max_length=1800, null=True)
    is_sold = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
>>>>>>> origin/main

    def __str__(self):
        return self.title

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_item"
        app_label = "core"
