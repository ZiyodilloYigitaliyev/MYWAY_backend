from django.contrib import admin
from .models import *
admin.site.register(ServiceAddres),
admin.site.register(TexServiceOrder),
admin.site.register([Gas, CarOil]),
admin.site.register(TexServiceMessage),

