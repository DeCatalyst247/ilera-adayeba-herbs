from django.contrib import admin

# Register your models here.
from .models import BlogCategory, BlogPost

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'slug'
    )

    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'published',
        'created_at'
    )

    list_filter = (
        'published',
        'category'
    )

    search_fields = (
        'title',
        'content'
    )

    prepopulated_fields = {
        'slug': ('title',)
    }