from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Feed
# Register your models here.
admin.site.register(Feed)

admin.site.unregister(Group)