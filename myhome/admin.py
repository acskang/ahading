from django.contrib import admin
from myhome.models import WEB_DOCUMENT

# Register your models here.
class viewAdmin(admin.ModelAdmin):
  list_display = ('id', 'category', 'title', 'content')
admin.site.register(WEB_DOCUMENT, viewAdmin)