from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    user = models.ForeignKey(User)
    edited = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
        ordering = ['-created']
        verbose_name_plural = "Posts"
        verbose_name = "Post"
