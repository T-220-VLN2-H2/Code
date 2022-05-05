from django.db import models
from django.contrib.auth.models import User
import core.models as core


class UserSales(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(core.Item)

    def __str__(self):
        return self.user_id.first_name

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_user_sales"
        app_label = "core"
