from django.contrib import admin

from qwertyindex.models import qwertyindex, Subscibemodel


# Register your models here.
@admin.register(qwertyindex)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'github_url',
        'github_project_url'
    )
    search_fields = (
        'name',
        'github_url',
        'github_project_url'
    )


@admin.register(Subscibemodel)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'email',
    )
    search_fields = (
        'email',
    )
