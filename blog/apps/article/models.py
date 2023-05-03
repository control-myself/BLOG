from django.db import models
from markdownx.models import MarkdownxField
from blog.apps.account.models import User


class Article(models.Model):
    title = models.CharField()
    author = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    content = MarkdownxField(default=None)
    pub_date = models.DateTimeField(auto_now_add=True)
    recommended_value = models.IntegerField(default=1)