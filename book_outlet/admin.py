from django.contrib import admin

from .models import Book

# Register your models here.

# add advanced settings in class


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    # does same stuff our save method does
    # base of type of a field.. if its slug, calls slugify under the hood and pre populates it
    prepopulated_fields = {"slug": ("title",)}
    # add filter fields you want to filter by in django admin
    list_filter = ("author", "rating")
    list_display = ("title", "author")


admin.site.register(Book, BookAdmin)