from django.db import models
from django.conf import settings
from django.utils import timezone
from sqlalchemy import UniqueConstraint


class Quiz(models.Model):
    """
    Represents a quiz entry in the database.

    Attributes:
        user (ForeignKey): The user who took the quiz.
        quiz_type (CharField): The type of the quiz.
        score (IntegerField): The score obtained in the quiz.
        date (DateTimeField): The date and time when the quiz was taken.

    Meta:
        constraints (list): A list of constraints for the Quiz model.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="Quiz_user",
        blank=True,
        null=True,
    )
    quiz_type = models.CharField(max_length=20)
    score = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
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
        """
        Returns a string representation of the Quiz object.

        Returns:
            str: The string representation of the Quiz object.
        """
        return f"User: {self.user} got: {self.score} in quiz: {self.quiz_type}"

    def save(self, *args, **kwargs):
        """
        Saves the Quiz object to the database.

        Overrides the default save() method to handle uniqueness and date updating.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if Quiz.objects.filter(
            user=self.user, quiz_type=self.quiz_type, score=self.score
        ).exists():
            # Existing quiz found, update the date instead of creating a new entry
            self.date = timezone.now
        else:
            # No existing quiz found, create a new entry
            super().save(*args, **kwargs)
