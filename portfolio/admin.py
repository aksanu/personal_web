from django.contrib import admin
from . import models
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display= ['name','email','message','created'] 

class StudentAdmin(admin.ModelAdmin):
	list_display= ['first_name','last_name'] 
admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.Student, StudentAdmin)