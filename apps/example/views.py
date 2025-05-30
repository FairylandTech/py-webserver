from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from django.http import HttpRequest

from fairylandfuture.structures.http.response import ResponseStructure
from fairylandfuture.interface.drf.response import DRFResponseMixin
from utils.journal import journal

namespace = "example"


class ExampleViewSet(GenericViewSet, DRFResponseMixin):

    @action(methods=["GET"], url_path="test", url_name="示例接口", detail=False)
    def test(self, request):
        journal.info("URL请求参数: {}", request.query_params)
        journal.info("请求体: {}", request.data)
        journal.info("请求文件: {}", request.FILES)
        journal.info("请求头: {}", request.headers)
        journal.info("请求方法: {}", request.method)
        journal.info("请求路径: {}", request.path)
        journal.info("请求完整路径: {}", request.get_full_path())
        journal.info("请求IP: {}", request.META.get("REMOTE_ADDR", "未知IP"))
        journal.info("请求用户: {}", request.user if request.user.is_authenticated else "未认证用户")

        data = ResponseStructure()

        data.code = 200
        data.message = "示例接口成功"
        data.data = {"example": "This is an example response from the ExampleViewSet."}

        return self._response(data)

    @action(methods=["POST"], url_path="submit", url_name="提交示例", detail=False)
    def submit(self, request: Request):
        journal.info("请求头: {}", request.headers)
        journal.info("提交数据: {}", request.data)
        files = request.FILES
        if files:
            journal.info("提交文件: {}", {file.name: file.size for file in files.values()})

        else:
            journal.info("没有提交文件")

        data = ResponseStructure()
        data.code = 201
        data.message = "提交成功"
        data.data = {"received_data": {}}

        return self._response(data)
