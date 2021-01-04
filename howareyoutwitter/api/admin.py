from django.contrib import admin
from api import models

@admin.register(models.Token)
class TokenAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Tweet)
class TweetAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    pass
