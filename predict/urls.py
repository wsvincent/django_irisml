from django.urls import path

from .views import predict

urlpatterns = [
    path("", predict, name="predict"),
]
