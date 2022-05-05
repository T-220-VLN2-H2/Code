from django.db import models


class ShippingDetails(models.Model):
    full_name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    postal_code = models.SmallIntegerField()
    city = models.CharField(max_length=128)

    def __str__(self):
        return self.full_clean

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_shipping_details"
        app_label = "core"
