from django.contrib import admin
from rango.models import Category, Page, UserProfile

# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'views', 'likes', 'slug')

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views')

# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)