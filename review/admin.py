from django.contrib import admin

from .models import Review, Rating

admin.site.register(Rating)
admin.site.register(Review)
