from django.db import models
from .user import User
# import order


class OrderHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO: add orderArray
    # order_array: Array<Order>

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "core_order_history"
        app_label = "core"
