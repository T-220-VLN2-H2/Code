from django.db import models


class PaymentInfo(models.Models):
    cardholder_name = models.CharField()
    card_number = models.CharField()
    cvc = models.CharField()
    expiry_month = models.IntegerField()
    expiry_year = models.IntergerField()

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "firesale_payment_info"
        app_label = "firesale"
