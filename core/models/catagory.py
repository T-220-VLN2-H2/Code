from django.db import models


class Catagory(models.Models):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    # TODO:
    # sub_categories = models.Array<Category>()

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "firesale_catagory"
        app_label = "firesale"
