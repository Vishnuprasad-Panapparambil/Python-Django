from django.contrib import admin

# Register your models here.
from .models import Mobile,Brand
admin.site.register(Brand)
admin.site.register(Mobile)
