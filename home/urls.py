from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('blog', views.blogPage, name='blogPage'),
    path('post/<str:pk>', views.post, name='post'),
    path('about', views.about, name='aboutPage'),
    

    #post urls
    path('newpost', views.newPost, name='newPost'),
    path('editpost/<str:pk>', views.editPost, name='editPost'),
    path('deletepost/<str:pk>', views.deletePost, name='deletePost'),

    #comment urls
    path('deletecomment/<str:pk>', views.deleteComment, name='deleteComment'),

]
