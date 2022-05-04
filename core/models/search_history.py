from django.db import models
from .user import User


class SearchHistory(models.Model):
    search_string = models.CharField(max_length=128)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "core_search_history"
        app_label = "core"
