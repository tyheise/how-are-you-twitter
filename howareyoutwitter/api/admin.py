from django.contrib import admin
from api import models

class TokenAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Token, TokenAdmin)
