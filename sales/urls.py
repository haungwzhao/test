from django.urls import path

from .views import listcustomers

urlpatterns = [
    path('orders/', listcustomers),
]