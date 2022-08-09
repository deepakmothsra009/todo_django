from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Task(models.Model):
    """
        Task model keeps the information of tasks
        ---
        Contains the definition of Table and it's attributes
    """


    STATE_CHOICES = (
        (0, 'TODO'),
        (1, 'In Progress'),
        (2, 'Done')
    )

    # which user created the entry
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # title of the task
    title = models.CharField(max_length=200)
    # description of the task 
    description = models.TextField(null=True, blank=True)
    # status is to keep the information of completion
    status = models.IntegerField(choices=STATE_CHOICES, default=0)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-title','-author')
