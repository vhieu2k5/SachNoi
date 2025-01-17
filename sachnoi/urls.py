from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('index.html', views.home, name='home'),  
    path('discover.html', views.discover, name='discover'),  
    path('author.html', views.author, name='author'),  
    path('category.html', views.category, name='category'),  
    path('login.htm',views.login, name='login'),
    path('signup.htm',views.signup, name='signup'),
    path('forgot-password.html', views.forgot_password, name='forgot_password'),
    path('account.html', views.account, name='account'),
    path('book_history.html', views.book_history, name='book_history'),
    path('favorite_books.html', views.favorite_books, name='favorite_books'),
    path('saved_book.html', views.saved_book, name='saved_book'),
    path('enter_OTP_code.html', views.enter_OTP_code, name='enter_OTP_code'),
    path('convert/<int:text_id>/', views.convert_text_to_speech, name='convert_text_to_speech'),
    path('create-entry/', views.create_text_entry, name='create_entry'),
    path('testapi/',views.testapi , name='testapi')
    
]