import django_filters

from adminapp.models import Book

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model=Book
        fields=['bookname','author','category','language']
