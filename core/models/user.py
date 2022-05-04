from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=128)
    user_name = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "core_user"
        app_label = "core"
