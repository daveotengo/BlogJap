from django import forms

from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = '__all__'
        fields = [
            "comment_author_email",
            "comment_author",
            "comment_content"]
        widgets = {
            #'comment_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'comment_author_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'comment_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Authour'}),
            'comment_content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
            #'comment_post': forms.TextInput(attrs={'class': 'form-control', 'hidden':True,'placeholder': 'Post'}),

        }

        # comment_title = models.CharField(max_length=50)
        # comment_author = models.CharField(max_length=50)
        # comment_content = models.TextField(max_length=500)
        # comment_author_email = models.EmailField(max_length=50)
        # comment_status = models.BooleanField(default=False)
        # comment_post = models.ForeignKey(to=Post, on_delete=models.CASCADE)  # manytoone
        # create_date = models.DateTimeField(auto_now_add=True)