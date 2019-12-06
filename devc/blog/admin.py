from django.contrib import admin
from .models import Post, Comment, Category

@admin.register(Post)
class PostDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',   
                       'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin): 
    list_display = ('post', 'created', 'active') 
    list_filter = ('active', 'created', 'updated') 
    search_fields = ('author', 'body') 
