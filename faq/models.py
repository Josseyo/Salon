from django.db import models


class Question(models.Model):
    """Model representing a question."""
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the string representation of the question."""
        return self.question

    @property
    def get_answer(self):
        """Return the associated answer, if it exists."""
        try:
            return self.answer
        except Answer.DoesNotExist:
            return None


class Answer(models.Model):
    """Model representing an answer to a question."""
    question = models.OneToOneField(
        Question,
        related_name='answer',
        on_delete=models.CASCADE
    )
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the string representation of the answer."""
        return f"Answer to: {self.question.question}"
