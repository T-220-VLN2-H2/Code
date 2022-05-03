from django.db import models
from .user import User


class SearchHistory(models.Models):
    search_string = models.CharField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "firesale_search_history"
        app_label = "firesale"
