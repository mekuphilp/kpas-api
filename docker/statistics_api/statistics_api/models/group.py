from django.db import models
from statistics_api.definitions import MYSQL_VARCHAR_DEFAULT_LENGTH
from statistics_api.models.base_model import BaseModel
from statistics_api.models.group_category import GroupCategory


class Group(BaseModel):
    canvas_id = models.IntegerField()
    name = models.CharField(max_length=MYSQL_VARCHAR_DEFAULT_LENGTH)
    group_category = models.ForeignKey(GroupCategory, on_delete=models.CASCADE)  # group_category id
    description = models.CharField(max_length=MYSQL_VARCHAR_DEFAULT_LENGTH, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    members_count = models.IntegerField()

    class Meta:
        db_table = "group"
