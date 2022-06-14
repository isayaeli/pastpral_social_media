
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Feed,Comment
# Register your models here.
admin.site.register(Feed)
admin.site.register(Comment)

admin.site.site_header = 'PSM admin'

admin.site.unregister(Group)