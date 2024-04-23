from django.contrib import admin, messages
from django.db import transaction

from .models import Pages


@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    exclude = ('url',)
    list_display = ["name", "slug", "url", "parent"]

    def save_model(self, request, obj, form, change):

        url = "/" + obj.slug if obj.slug else ""

        if obj.parent:
            url_parent = Pages.objects.filter(id=obj.parent.pk).first().url
            url = url_parent[:-1] + url

        obj.url = url + "/"
        super().save_model(request, obj, form, change)
