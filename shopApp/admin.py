from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.gameList)
admin.site.register(models.gameDetails)
admin.site.register(models.shoppingCart)
admin.site.register(models.orders)
