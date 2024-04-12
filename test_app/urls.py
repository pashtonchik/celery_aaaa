from django.urls import path
from rest_framework import routers

from test_app.api import aaa

router = routers.DefaultRouter()

urlpatterns = [
    path('api/v2/client/auth/', aaa)
]