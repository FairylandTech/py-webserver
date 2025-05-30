# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-28 18:04:52 UTC+08:00
"""

from django.db import models


class RBACGroupModel(models.Model):

    name = models.CharField(max_length=64, verbose_name="用户组名")
    parent_id = models.IntegerField(default=0, verbose_name="父用户组ID")
    description = models.CharField(max_length=256, blank=True, default="", verbose_name="描述")

    existed = models.BooleanField(default=True, verbose_name="是否存在")
    created_at = models.DateTimeField(auto_now_add=timezone.now, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        managed = False
        db_table = "app_rbac_group"
        unique_together = [["name", "parent_id"]]
        verbose_name = "用户组"
        verbose_name_plural = "用户组"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        seif.name = self.name.strip()
        self.description = self.description.strip()

        super().save(
            *args,
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )
