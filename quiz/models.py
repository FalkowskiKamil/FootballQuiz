from django.db import models
from django.conf import settings
from django.utils import timezone
from sqlalchemy import UniqueConstraint


class Quiz(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="Quiz_user",
        blank=True,
        null=True,
    )
    quiz_type = models.CharField(max_length=20)
    score = models.IntegerField()
    date = models.DateTimeField(default=timezone.now())
    __table_args__ = (
        UniqueConstraint(
            "score", "user", "quiz_type", name="unique_score_user_quiz_type"
        ),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "quiz_type", "score"],
                name="unique_score_user_quiz_type",
            )
        ]

    def __str__(self):
        return f"User: {self.user} got: {self.score} in quiz: {self.quiz_type}"

    def save(self, *args, **kwargs):
        if Quiz.objects.filter(
            user=self.user, quiz_type=self.quiz_type, score=self.score
        ).exists():
            # Existing quiz found, update the date instead of creating a new entry
            self.date = timezone.now()
        else:
            # No existing quiz found, create a new entry
            super().save(*args, **kwargs)
