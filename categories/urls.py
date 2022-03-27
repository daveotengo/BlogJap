from django.urls import path

from . import views

urlpatterns = [

    path('<int:category_id>/', views.category_detail , name='category_detail'),

]
