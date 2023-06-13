from django.db import models
from django.db.models import CASCADE
from users.models import User
from posts.models import Post
from django.utils import timezone


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True)

