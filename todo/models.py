from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CHOICES = (
        (1, 'Done'),
        (2, 'Doing'),
        (3, 'Undone'),
    )
    title = models.CharField(max_length=20)
    description = models.TextField()
    condition = models.SmallIntegerField(choices=CHOICES, default=3)

    def __str__(self):
        return self.title
