from django.contrib import admin

from books.models import Book,Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','book','content','datetime_create']
# Register your models here.
admin.site.register(Book)
admin.site.register(Comment,CommentAdmin)

