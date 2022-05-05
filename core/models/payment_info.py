from django.db import models


class PaymentInfo(models.Model):
    cardholder_name = models.CharField(max_length=128)
    card_number = models.CharField(max_length=16)
    cvc = models.CharField(max_length=3)
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()

    def __str__(self):
        return self.cardholder_name

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_payment_info"
        app_label = "core"
