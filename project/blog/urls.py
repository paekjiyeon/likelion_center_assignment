from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name='create'),
    path('modify/<int:blog_id>', views.modify, name="modify"),
    path('delete/<int:blog_id>', views.delete, name = 'delete'),
    path('modify/<int:post_id>', views.modify, name='modify'),
    path('comment_write/<int:blog_pk>/', views.comment_write, name='comment_write'),
    path('comment_delete/<int:blog_id>/<int:comment_id>',views.comment_delete, name="comment_delete"),
    
]
