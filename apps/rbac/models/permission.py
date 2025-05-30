# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-28 16:07:26 UTC+08:00
"""

from django.db import models
from django.core.exceptions import ValidationError


class PermissionModel(models.Model):

    # name = models.CharField(max_length=255, unique=True, verbose_name="权限名称", help_text="权限的可读名称，如：查看用户列表")
    # code = models.CharField(max_length=255, unique=True, verbose_name="权限代码", help_text="权限的唯一标识符，如：view_user_list, 000001")
    # description = models.TextField(blank=True, null=True, verbose_name="权限描述", help_text="对权限的详细描述")
    # path = models.CharField(max_length=255, unique=True, verbose_name="权限路径", help_text="权限对应的URL路径或API端点，如：/api/users/list")

    name = models.CharField(max_length=64, verbose_name="权限名")
    description = models.CharField(max_length=256, blank=True, null=True, verbose_name="权限描述")
    code = models.CharField(max_length=64, verbose_name="权限代码")
    path = models.CharField(max_length=256, verbose_name="API路径")

    existed = models.BooleanField(default=True, verbose_name="权限是否存在", help_text="标识该权限是否仍然有效")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="最后一次更新的时间")

    class Meta:
        managed = False
        db_table = "app_rbac_permission"
        verbose_name = "权限"
        verbose_name_plural = "权限"
        ordering = ["-updated_at"]
        # unique_together = ("path", "code")
        # indexes = [
        #     models.Index(fields=["path"]),
        #     models.Index(fields=["code"]),
        #     models.Index(fields=["name"]),
        # ]

    def __str__(self):
        return f"{self.name} ({self.code}): {self.path}"

    def clean(self):
        super().clean()

        if not self.path.startswith("/"):
            raise ValidationError({"path": "权限路径必须以 '/' 开头"})

        if not self.code.isidentifier():
            raise ValidationError({"code": "权限代码必须是有效的标识符，且只能包含字母、数字和下划线"})

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.code = self.code.strip().lower()
        self.name = self.name.strip()
        self.path = self.path.rstrip("/") + ("/" if self.path != "/" else "")  # 去掉末尾的 '/'

        super().save(*args, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
