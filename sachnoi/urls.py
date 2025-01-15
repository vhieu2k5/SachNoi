from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('index.html', views.home, name='home'),  
    path('discover.html', views.discover, name='discover'),  
    path('author.html', views.author, name='author'),  
    path('category.html', views.category, name='category'),  
]