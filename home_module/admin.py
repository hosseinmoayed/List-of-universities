from django.contrib import admin

# Register your models here.
from home_module.models import City , Country , University

admin.site.register(City)
admin.site.register(Country)
admin.site.register(University)