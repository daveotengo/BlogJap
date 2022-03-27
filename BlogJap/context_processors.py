from categories.models import Category


def context_processor(request):
    categories = Category.objects.all()[:8]
    context = {
        'categories':categories
    }
    #context['data'] = 'Some data'
    return context