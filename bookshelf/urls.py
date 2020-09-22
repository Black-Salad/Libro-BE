from django.urls import path
from bookshelf import views

app_name = 'bookshelf'
urlpatterns = [
    path('', views.BookList.as_view()),
    path('<int:pk>/', views.BookDetail.as_view()),
    path('shelf/', views.ShelfList.as_view()),
    path('shelf/join/', views.BookShelfJoinList.as_view()),
]
