from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, default='Generic')
    color = models.CharField(max_length=10, default='primary')

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    task_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE, 
        related_name='tasks',
        null=True, 
        blank=True 
    )
