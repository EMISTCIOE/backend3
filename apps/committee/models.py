from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Member(models.Model):
    sno = models.IntegerField(
        verbose_name="S.No.",
        validators=[
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=25),
        ]
    )
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    batch = models.CharField(max_length=15)
    # image_link = models.CharField(max_length=150, blank=True, null=True, verbose_name="Photo Link")
    image = models.ImageField(upload_to='committee_members/', blank=True, null=True)

    class Meta:
        ordering = ['sno']

    def __str__(self):
        return self.name

