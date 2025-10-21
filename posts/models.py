from django.db import models
import uuid


# Create your models here.
class Post(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
