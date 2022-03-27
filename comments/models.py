from django.db import models

# Create your models here.
from posts.models import Post


class Comment(models.Model):
    #comment_title = models.CharField(max_length=50)
    comment_author = models.CharField(max_length=50)
    comment_content = models.TextField(max_length=500)
    comment_author_email = models.EmailField(max_length=50)
    comment_status = models.BooleanField(default=False)
    comment_post = models.ForeignKey(to=Post, on_delete=models.CASCADE)#manytoone
    create_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.comment_content
