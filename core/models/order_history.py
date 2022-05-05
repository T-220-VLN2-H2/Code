from django.db import models
from .user import User

# from .order import order


class OrderHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO: add orderArray
    # order_array: Array<Order>

    def __str__(self):
        return self

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_order_history"
        app_label = "core"
