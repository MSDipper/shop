from django.contrib import admin
from django.utils.safestring import mark_safe
from blog.models import Category, Tag, Ip, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',), }
    save_as = True
    save_on_top = True
   

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',), }
    save_as = True
    save_on_top = True 
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'get_image', 'author', 'category', 'create_at']
    list_filter  = ( 'title', 'category', 'author', 'create_at' )
    search_fields  = ( 'title' , 'category__name')
    prepopulated_fields = {'slug': ('title',), }
    save_as = True
    save_on_top = True 

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="48">')
    
    get_image.short_description = "Изображение"
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'parent', 'publish']
    list_filter  = ( 'name', 'parent', 'publish')
    search_fields  = ('name',)


admin.site.register(Ip)
admin.site.site_title = 'Админ панель'
admin.site.site_header = 'Админ панель'
