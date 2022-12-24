from django.contrib import admin
from .models import Customer,User,UserProfile
from main.models import Mails,Messages

# Register your models here.

admin.site.register(Customer)
admin.site.register(Mails)
admin.site.register(Messages)
admin.site.register(User)
admin.site.register(UserProfile)