from django.db import models


class User(models.Models):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField()
    user_name = models.CharField()
    email = models.EmailField()
    password = models.CharField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "firesale_user"
        app_label = "firesale"
