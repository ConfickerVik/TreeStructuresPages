from __future__ import annotations

from django.contrib import admin, messages
from django.db import transaction

from .models import Pages


@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    exclude = ('url',)
    list_display = ["name", "slug", "url", "parent"]

    def generate_url(self, slug: str = None, parent_id: int = None) -> str:
        url = "/" + slug if slug else ""
        if parent_id:
            url_parent = Pages.objects.filter(id=parent_id).first().url
            url = url_parent[:-1] + url
        return url + "/"

    def changes_children_url(self, pages: Pages, children_to_update: list, slug: str | None, new_slug: str | None):

        tmp_slug = slug

        if not new_slug:
            tmp_slug = f"/{slug}"
            new_slug = ""

        for children in pages.children.all().iterator():
            children.url = children.url.replace(tmp_slug, new_slug) if slug else f"/{new_slug}{children.url}"
            children_to_update.append(children)
            self.changes_children_url(
                pages=children,
                slug=slug,
                new_slug=new_slug,
                children_to_update=children_to_update
            )

    def save_model(self, request, obj, form, change):
        obj.url = self.generate_url(slug=obj.slug, parent_id=obj.parent_id)
        if change:
            old_slug = Pages.objects.get(id=obj.id).slug
            if old_slug != obj.slug:
                children_to_update = []
                self.changes_children_url(
                    pages=obj,
                    slug=old_slug,
                    new_slug=obj.slug,
                    children_to_update=children_to_update
                )
                if children_to_update:
                    Pages.objects.bulk_update(
                        children_to_update,
                        ['url']
                    )

        super().save_model(request, obj, form, change)
