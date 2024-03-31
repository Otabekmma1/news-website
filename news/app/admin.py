from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'updated', 'category', 'published', 'image')
    list_display_links = ('title',)
    list_editable = ('published', 'category')
    list_filter = ('published',)
    search_fields = ('title', 'content')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
