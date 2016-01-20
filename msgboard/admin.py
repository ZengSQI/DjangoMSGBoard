from django.contrib import admin

from .models import MsgPost, Comment

admin.site.register(MsgPost)
admin.site.register(Comment)
