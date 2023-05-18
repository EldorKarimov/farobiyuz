from django.contrib import admin

from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug':('name', )}
    search_fields = ['name', 'id']
    ordering = ('-id', )

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'category']
    search_fields = ['full_name', 'email', 'category']
    ordering = ('-id', )

@admin.register(Skils)
class SkilsAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name', )}
    search_fields = ['name']
    ordering = ('-id',)

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at', 'category']
    prepopulated_fields = {'slug':('name', )}
    search_fields = ['name', 'created_at', 'category']
    ordering = ('-id',)

@admin.register(MessageFromUser)
class MessageFromUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    search_fields = ['name', 'phone', 'email']
    ordering = ('-id',)