from django.db import models
class News(models.Model):
    article = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.article 
