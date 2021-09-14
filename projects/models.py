from django.db import models
from django.db.models.lookups import GreaterThan
import uuid





class Project(models.Model):
    title = models.CharField(max_length=200)
    startdate = models.DateField(null=False, blank=False)
    enddate = models.DateField(null=False, blank=False)
    value = models.BigIntegerField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)



    def __str__(self):
        return self.title
