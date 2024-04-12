from django.db import models

# Create your models here.
from django.db import models
from Mcq.models import Question
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Bookmark(models.Model):
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Assuming you're using Django's built-in user model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return f"Bookmark {self.id} by {self.user}"
    


class BookmarkQuestion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'question')

    def __str__(self):
        return f"{self.user.username} bookmarked questions {self.question.question}"

class SolvedQuestions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    solved_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=255, blank=True, null=True)
    is_correct = models.BooleanField(default=False, null=True)
    last_answered = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'solved_question')

    def __str__(self):
        return f"{self.user.username} solved {self.solvedquestion.question}"
class UnsolvedQuestions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    unsolved_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)  # Tracks the last access time

    class Meta:
        unique_together = ('user', 'unsolved_question')  

    def __str__(self):
        return f"{self.user.username} unsolved {self.unsolvedquestion.question}"

