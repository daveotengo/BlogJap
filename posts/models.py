
# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from categories.models import Category


class Post(models.Model):

    #post_id=models.CharField(max_length=50,unique=True)
    post_title=models.CharField(max_length=50)
    post_content=models.TextField(max_length=225)
    post_status= models.BooleanField(default=False)
    post_image = models.ImageField(upload_to='post_images',null=True)

    post_category= models.ForeignKey(Category, on_delete=models.CASCADE)#manytoone
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)#manytoone
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True)



    class Meta:
        managed = True
        db_table = 'post'

    #list_display = ['game_id', 'enable', 'port']

    #list_display = [field.name for field in GameInfo._meta.get_fields()]
    def __str__(self):
        return self.post_content