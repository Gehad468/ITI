from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list',views.book_list, name='book_list'),
    path('add',views.book_add, name='book_add'),
    path('update/<str:name>',views.book_update, name='book_update'),
    path('delete/<int:id>',views.book_delete, name='book_delete'),
    path('Show/<int:id>',views.book_show, name='book_show'),
    
]

