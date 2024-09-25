from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        deadline_info = self.deadline.strftime("%Y-%m-%d %H:%M") if self.deadline else "No deadline"
        return f"Task: {self.content} (created: {self.created_at.strftime('%Y-%m-%d %H:%M')}, deadline: {deadline_info})"