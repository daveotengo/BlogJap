from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    #cat_id = models.CharField(max_length=225)
    cat_title = models.CharField(max_length=225)
    cat_image = models.ImageField(upload_to='cat_images',null=True)

    create_by = models.ForeignKey(User, on_delete=models.CASCADE)#manytoone
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True)



    def __str__(self):
        return self.cat_title