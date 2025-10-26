from django.db import models
from django.utils import timezone
import uuid

class PhotoLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=75)
    url = models.CharField(verbose_name="Link", max_length=150)
    date = models.DateField(default=timezone.now)
    
    # Add a field to represent the status (whether to show or not)
    is_visible = models.BooleanField(default=True, verbose_name="Is Visible")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Photo Link"
        verbose_name_plural = "Photo Links"
        ordering = ['-date']