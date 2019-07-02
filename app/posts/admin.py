from .models import Post
from django.contrib import admin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created_at',
        'user',
        'likes_count',
    )
    list_select_related = (
        'user',
    )
    list_per_page = 50
    ordering = ['-created_at']

    def likes_count(self, obj):
        return obj.likes.count()
