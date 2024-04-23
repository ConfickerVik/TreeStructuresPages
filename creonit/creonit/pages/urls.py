from django.urls import path
from .views import PageListChildrenView


urlpatterns = [
    path('pages/', PageListChildrenView.as_view()),
]
