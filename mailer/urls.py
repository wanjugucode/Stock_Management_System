from django.urls import path
from .views import send_order_mail

urlpatterns = [
    path('',send_order_mail)
]
