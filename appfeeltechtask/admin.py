from django.contrib import admin
from .models import User,Inquiry

# Register your models here.
@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name']

@admin.register(Inquiry)
class Useradmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','contact','subject']
