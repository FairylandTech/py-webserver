from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.decorators import action

from fairylandfuture.structures.http.response import ResponseStructure
from fairylandfuture.interface.drf.response import DRFResponseMixin
from utils.journal import journal

namespace = "example"


class ExampleViewSet(GenericViewSet, DRFResponseMixin):

    @action(methods=["GET"], url_path="test", url_name="示例接口", detail=False)
    def test(self, request, *args, **kwargs):
        journal.debug("示例API")
        journal.debug("请求: {}, type: {}", request, type(request))

        data = ResponseStructure()

        data.code = 200
        data.message = "示例接口成功"
        data.data = {
            "example": "This is an example response from the ExampleViewSet."
        }

        return self._response(data)
