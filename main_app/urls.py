from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.book_index, name='book_index'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/create/', views.BookCreate.as_view(), name='book_create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
    path('books/<int:book_id>/add_comment/', views.add_comment, name='add_comment'),
    path('accounts/signup/', views.signup, name='signup'),







]


