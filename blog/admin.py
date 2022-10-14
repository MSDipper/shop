from django.contrib import admin

from blog.models import Category, Tag, Ip, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    save_as = True
    save_on_top = True
    
   

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    save_as = True
    save_on_top = True 
    


   

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    save_as = True
    save_on_top = True 




admin.site.register(Ip)
admin.site.register(Comment)
