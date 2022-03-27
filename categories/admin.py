from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from categories.models import Category


class CategoryAdmin(admin.ModelAdmin):

    list_display = [field.attname for field in Category._meta.fields]

    exclude = ("modify_date ",)
    readonly_fields = ('modify_date',)
    # def get_queryset(self, request):
    #     qs = super(CategoryAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(create_by=request.user)
    # def get_readonly_fields(self, request, obj=None):
    #     if obj is None:
    #         return ['modify_date']
    #     return []

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'create_by':
             kwargs["queryset"] = User.objects.filter(username=request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category,CategoryAdmin)