from django.contrib import admin

from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # pass
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = (
        "author",
        "rating",
    )
    list_display = (
        "title",
        "author",
    )


admin.site.register(Book, BookAdmin)
