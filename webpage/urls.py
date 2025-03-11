from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='homepage'),
    path('signup', views.signup, name='signuppage'),
    path('login', views.login, name='loginpage'),
    path('userlist', views.userlist, name='userlist'),
    path('blog', views.blog, name='blogpage'),
    path('posting', views.create_post, name='postpage')
]