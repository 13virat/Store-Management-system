from django.db import models


# Create your models here.
class Stock(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(null=True, blank=True, default="0")
    receive_quantity = models.IntegerField(null=True, blank=True, default="0")
    receive_by = models.CharField(max_length=50, null=True, blank=True)
    issue_quantity = models.IntegerField(null=True, blank=True, default="0")
    issue_by = models.CharField(max_length=50, null=True, blank=True)
    issue_to = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(null=True, blank=True, default="0")
    last_updated_by = models.DateTimeField(auto_now_add=False, auto_now=True)
    export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name
