# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-28 17:34:36 UTC+08:00
"""

from django.db import models
from django.core.exceptions import ValidationError
from apps.rbac.models.permission import PermissionModel


class RoleModel(models.Model):

    name = models.CharField(max_length=32, unique=True, verbose_name="角色名称", help_text="角色名称")
    description = models.CharField(max_length=128, blank=True, null=True, verbose_name="角色描述", help_text="角色描述")
    permissions = models.ManyToManyField(PermissionModel, blank=True, related_name="roles", verbose_name="权限", help_text="角色拥有的权限")
    systemd = models.BooleanField(default=False, verbose_name="系统角色", help_text="是否为系统内置角色，系统角色不可删除")
    # priority = models.IntegerField(default=0, verbose_name="优先级", help_text="角色的优先级，数值越大优先级越高")

    existed = models.BooleanField(default=True, verbose_name="是否存在", help_text="角色是否存在")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="角色创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="角色最后更新时间")

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = "角色"
        db_table = "rbac_app_role"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()

        if self.systemd:
            reserved_names = ["系统管理员", "admin", "superuser", "system"]
            if self.name not in reserved_names and not self.pk:
                raise ValidationError({"name": "系统角色名称不规范"})

    def get_permissions(self) -> models.query.QuerySet:
        return self.permissions.filter(existed=True)

    def get_permissions_count(self) -> int:
        return self.permissions.filter(existed=True).count()

    def has_permission(self, code) -> bool:
        return self.permissions.filter(code=code, existed=True).exists()

    def add_permission(self, code):
        try:
            permission = self.permissions.get(code=code, existed=True)
        except PermissionModel.DoesNotExist:
            raise ValidationError(f"Permission with code '{code}' does not exist or is not active.")

        self.permissions.add(permission)

    def remove_permission(self, code):
        try:
            permission = self.permissions.get(code=code, existed=True)
        except PermissionModel.DoesNotExist:
            raise ValidationError(f"Permission with code '{code}' does not exist or is not active.")

        self.permissions.remove(permission)
