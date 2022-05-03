from django.db import models


class ShippingDetails(models.Models):
    full_name = models.CharField()
    address = models.CharField()
    postal_code = models.SmallIntegerField()
    city = models.CharField()

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "firesale_shipping_details"
        app_label = "firesale"
