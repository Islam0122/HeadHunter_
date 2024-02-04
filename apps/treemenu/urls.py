from django.urls import path
from .views import Menu_View

urlpatterns = [
     path('', Menu_View.as_view(), name='menu_view'),
]
