from django.urls import path

from blog import views

urlpatterns = [
    path('' , views.index , name='index'),
    path('posts/' , views.posts , name='posts'),
    path('posts/<int:id>' , views.post , name='post'),
    path('search/', views.search_result, name="search_results"),
    path('register/', views.register, name="register"),
    path('posts/<int:id>/comment', views.comment, name='comment'),

]
