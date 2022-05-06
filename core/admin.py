from django.contrib import admin

# Register your models here.
import core.models as models

admin.site.register(models.Item)
admin.site.register(models.Profile)
admin.site.register(models.Category)
admin.site.register(models.Order)
