from django.contrib import admin
from .models import Customer
from main.models import Mails,Messages

# Register your models here.

admin.site.register(Customer)
admin.site.register(Mails)
admin.site.register(Messages)