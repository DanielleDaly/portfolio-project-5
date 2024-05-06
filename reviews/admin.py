from django.contrib import admin
from .models import Review

class ReviewsAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

    fields = ('product', 'title', 'author', 'content', 'source', 'source_url', 'date',)

    list_display = ('product', 'title', 'author', 'date',)

    ordering = ('-date',)

admin.site.register(Review, ReviewsAdmin)
