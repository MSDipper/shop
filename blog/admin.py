from django.contrib import admin

from blog.models import Category, Tag, Ip, Post, Comment

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Ip)
admin.site.register(Post)
admin.site.register(Comment)
