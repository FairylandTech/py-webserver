# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-27 15:27:51 UTC+08:00
"""

from pathlib import Path

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.example.views import ExampleViewSet

app_name = Path(__file__).resolve().parent.name

router = DefaultRouter(trailing_slash=False, use_regex_path=False)

router.register(r"/example", ExampleViewSet, basename="示例视图集")

urlpatterns = [
    path("/v1", include(router.urls)),
]