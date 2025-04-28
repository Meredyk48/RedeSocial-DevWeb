from django.contrib import admin
from .models import Post, Comment, Friendship

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Friendship)

# Register your models here.
