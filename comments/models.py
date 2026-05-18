from django.db import models
from django.conf import settings
from django.urls import reverse

# Comment model for blog posts
class Comment(models.Model):
    post = models.ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    body = models.TextField()
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='replies',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"Comment by {self.author or self.name} on {self.post}"

    def get_absolute_url(self):
        try:
            return reverse('posts:post_detail', kwargs={'pk': self.post.pk})
        except Exception:
            return '#'

