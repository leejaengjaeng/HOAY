from django.contrib import admin
from .models import *
# Register your models here.

# Register your models here.
class GwanjongAdmin(admin.ModelAdmin):
	list_display = ('word', 'value')

admin.site.register(Gwanjong, GwanjongAdmin)