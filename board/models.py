from django.db import models

# Create your models here.
class Board(models.Model) : 
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self) : 
        return f'{self.title}, {self.content},{self.created_at},{self.updated_at}'