from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    @property
    def get_answer(self):
        try:
            return self.answer
        except Answer.DoesNotExist:
            return None

class Answer(models.Model):
    question = models.OneToOneField(Question, related_name='answer', on_delete=models.CASCADE)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer to: {self.question.question}"
