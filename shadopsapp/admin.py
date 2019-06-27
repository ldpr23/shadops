from django.contrib import admin
from shadopsapp.models import LineOfBusiness, Location, DesiredInfo, Employee

# Register your models here.
admin.site.register(LineOfBusiness)
admin.site.register(Location)
admin.site.register(DesiredInfo)
admin.site.register(Employee)
