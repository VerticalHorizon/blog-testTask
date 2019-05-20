from django.db import models
from django.contrib.auth import get_user_model

__all__ = ['Post', 'Reaction']


class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def likes(self):
        return self.reactions.filter(positive=True)

    @property
    def unlikes(self):
        return self.reactions.filter(positive=False)


class Reaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='reactions', on_delete=models.CASCADE)
    positive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
