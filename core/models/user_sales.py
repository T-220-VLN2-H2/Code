from django.db import models
from .user import User
# TODO: import item


class UserSales(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO:
    # items = models.Array<Item>

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "core_user_sales"
        app_label = "core"
