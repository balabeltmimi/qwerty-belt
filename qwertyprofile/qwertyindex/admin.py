from django.contrib import admin

from qwertyindex.models import qwertyindex

# Register your models here.
@admin.register(qwertyindex)
class ProfileAdmin(admin.ModelAdmin):
    pass