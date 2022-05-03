from django.db import models
# TODO: models.imprt item


class UserSales(models.Models):
    user_id = models.BigIntergerField()
    # TODO:
    # items = models.Array<Item>

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "firesale_user_sales"
        app_label = "firesale"
