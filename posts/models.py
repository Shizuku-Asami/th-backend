from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=500)
    summary = models.TextField()
    content = models.TextField()
    audio_url = models.URLField()
    audio_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
