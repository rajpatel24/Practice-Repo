from django.db import models

# Create your models here.


from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User


class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_text = models.TextField(max_length=200)
    blog_date = models.DateTimeField(auto_now_add=True)
    blog_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
        return f'{self.blog_title}'
