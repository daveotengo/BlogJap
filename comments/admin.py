from django.contrib import admin

# Register your models here.
from comments.models import Comment


class CommentsAdmin(admin.ModelAdmin):

    list_display = [field.attname for field in Comment._meta.fields]




admin.site.register(Comment,CommentsAdmin)