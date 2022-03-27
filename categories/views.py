from django.shortcuts import render

# Create your views here.
from categories.models import Category
from posts.models import Post


def category_detail(request,category_id):
    category = Category.objects.get(id=category_id)
    posts_by_category = Post.objects.filter(post_category=category)
    context = {
        'posts_by_category':posts_by_category

    }
    return render(request,'home.html',context)

