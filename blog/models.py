from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 20)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    db_null = models.IntegerField(null=True)
   

    def __str__(self):
        return self.title

        