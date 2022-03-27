from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from posts.models import Post


class PostsAdmin(admin.ModelAdmin):

    list_display = [field.attname for field in Post._meta.fields]
    exclude = ("modify_date ",)
    readonly_fields = ('modify_date',)
    # def get_queryset(self, request):
    #     qs = super(PostsAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'post_user':
             kwargs["queryset"] = User.objects.filter(username=request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:  # editing an existing object
    #         return self.readonly_fields + ('modify_date')
    #     return self.readonly_fields


admin.site.register(Post,PostsAdmin)