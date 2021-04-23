from django.contrib import admin
from blog.models import Post,Comment
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['title','image','date']
    list_filter = ['date']
    search_fields = ['title']
admin.site.register(Post,PostAdmin)

