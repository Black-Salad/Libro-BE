from django.contrib import admin
from .models import Book, Shelf, BookStar

# Register your models here.


# class BookAdmin(admin.ModelAdmin):
#     list_display = ('book_id', 'book_title', 'book_isbn')


# class ShelfAdmin(admin.ModelAdmin):
#     list_display = ('user_id', 'book_id', 'book_isbn')


admin.site.register(Book)
admin.site.register(Shelf)
admin.site.register(BookStar)
