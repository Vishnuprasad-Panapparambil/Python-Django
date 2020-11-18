import django_filters
from admin_side.models import Mobile


class SearchForm(django_filters.FilterSet):
    class Meta:
        model=Mobile
        fields ={
            'mobile_name':['exact'],
            'brand':['exact'],
            'price':['lt'],
        }