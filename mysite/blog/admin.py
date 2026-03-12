from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at','slug' , 'status' )
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author', 'status')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', 'created_at')
    date_hierarchy = 'created_at'
    raw_id_fields = ('author',)