from django.db import models

# Create your models here.

class Url(models.Model):
    link = models.CharField(max_length=10000, null=False, blank=False)
    uuid = models.CharField(("id") ,max_length=10, null=False, blank=False)

    def __str__(self) -> str:
        return self.link