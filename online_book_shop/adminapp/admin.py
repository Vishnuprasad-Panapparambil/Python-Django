from django.contrib import admin


from adminapp.models import Book,BookCategory
admin.site.register(Book)
admin.site.register(BookCategory)
