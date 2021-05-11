from django.urls import path
from .views import transfer, ActionListView


urlpatterns = [
    path('transfer/', transfer, name='transfer'),
    path('actions/', ActionListView.as_view(), name='actions')
]