from django.db import models
from .user import User


class Notification(models.Model):
    # TODO: add notification method
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128)
    message = models.CharField(max_length=280)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_question"
        app_label = "core"
