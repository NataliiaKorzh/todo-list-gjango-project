from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    def clean(self):
        super().clean()
        if self.deadline and timezone.is_aware(self.deadline):
            if self.deadline < timezone.now():
                raise ValidationError("Deadline cannot be before time of creation.")

    class Meta:
        ordering = ["status", "-datetime"]


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name
