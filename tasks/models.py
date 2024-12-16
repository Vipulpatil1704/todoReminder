# from django.db import models
from djongo import models
# Create your models here.
class Task(models.Model):
    app_label = 'tasks'
    _id = models.ObjectIdField()  # Djongo field for MongoDB ObjectId
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title
    def __str__(self):
        return f'title: {self.title}, description: {self.description}, completed: {self.completed}, created At: {self.created_at}, updated At: {self.updated_at}'
