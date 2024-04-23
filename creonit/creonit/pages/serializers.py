from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Pages


class PagesSerializer(serializers.ModelSerializer):
    children = SerializerMethodField()

    class Meta:
        model = Pages
        fields = ["name", "url", "children"]

    def get_children(self, obj):

        if obj.children.exists():
            return PagesSerializer(obj.children.all(), many=True).data

        return []
