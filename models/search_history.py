from django.db import models


class SearchHistory(models.Models):
    search_string = models.CharField()
    timestamp = models.DateTimeField()

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "firesale_search_history"
        app_label = "firesale"
