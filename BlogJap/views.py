import app as app
from django.shortcuts import render

import posts
from categories.models import Category
from comments.form import CommentForm
from posts.models import Post


def home_page(request):
    first_category = Category.objects.all().first()
    posts_by_category = Post.objects.filter(post_category=first_category)
    # forms = SubscriberForm()
    # if request.method == 'POST':
    #     forms = SubscriberForm(request.POST)
    #     if forms.is_valid():
    #         forms.save()
    context = {
        'posts_by_category': posts_by_category,
    #'forms': forms
    }
    return render(request, 'home.html', context)
    #return render(request, 'home.html')
def post_detail(request,post_id):
    forms = CommentForm()
    post_detail = Post.objects.get(id=post_id)

    if request.method == 'POST':
        print("=====post====")
        forms = CommentForm(request.POST)
        if forms.is_valid():
            print("=====valid====")
            instance = forms.save(commit=False)
            instance.comment_post = post_detail
            instance.save()
            #forms.save()
    context = {
        'post_detail':post_detail,
        'forms':forms,
    }
    return render(request,'single.html',context)


# @app.context_processor
# def inject_user():
#     return dict(app_name="APP_NAME")