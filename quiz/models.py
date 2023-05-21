from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.
class Quiz(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="Quiz_user",
        blank=True,
        null=True
    )
    quiz_type = models.CharField(max_length=20)
    score = models.IntegerField()
    date = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return f"{self.score}"