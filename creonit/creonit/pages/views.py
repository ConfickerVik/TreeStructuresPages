from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PagesSerializer

from .models import Pages


class PageListChildrenView(ListAPIView):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["url"]
