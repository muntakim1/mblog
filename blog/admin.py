from django.contrib import admin
from .models import Category, Post, AlgorithmCategory, AlgorithmPost


class CustomCategory(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CustomCategory)


class CustomAlgoCategory(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(AlgorithmCategory, CustomAlgoCategory)


class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description')
    date_hierarchy = 'dateTime'
    list_display = ('title', 'category')
    list_filter = ('title', 'category', 'dateTime')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)


class AlgoPostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description')
    date_hierarchy = 'dateTime'
    list_display = ('title', 'category')
    list_filter = ('title', 'category', 'dateTime')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(AlgorithmPost, AlgoPostAdmin)
