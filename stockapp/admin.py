from django.contrib import admin

# Register your models here.
from stockapp.models import Stock

admin.site.register(Stock)
