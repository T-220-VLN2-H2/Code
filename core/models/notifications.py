from django.db import models
from .user import User


class Notification(models.Models):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField()
    message = models.CharField()
    timestamp = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "polls_question"
        app_label = "polls"
