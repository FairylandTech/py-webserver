# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-28 15:56:05 UTC+08:00
"""

from pathlib import Path
from django.urls import path, include
from rest_framework.routers import SimpleRouter

app_name = Path(__file__).resolve().parent.name

router = SimpleRouter(trailing_slash=False, use_regex_path=False)

urlpatterns = [
    path("/v1", include(router.urls)),
]
