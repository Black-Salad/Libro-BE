from django.urls import path
from bookshelf import views

app_name = 'bookshelf'
urlpatterns = [
    path('', views.BookList.as_view()),
    path('<int:pk>/', views.BookDetail.as_view()),
    path('shelf/', views.ShelfList.as_view()),
    path('shelf/<int:pk>/', views.ShelfDetail.as_view()),
    path('shelf/count/', views.ShelfCount.as_view()),
    path('shelf/datefilter/', views.BookShelfDateFilterList.as_view()),
    path('star/', views.StarList.as_view()),
    path('star/count/', views.StarCount.as_view()),
    path('star/<int:pk>/', views.StarDetail.as_view()),
    path('shelf/join/', views.BookShelfJoinList.as_view()),
    path('shelf/join/note/', views.BookShelfJoinList2.as_view()),
    path('shelf/join/<int:cnt>', views.BookShelfJoinList.as_view()),
    path('star/join/', views.BookStarJoinList.as_view()),
    path('star/join/<int:cnt>', views.BookStarJoinList.as_view()),
    path('star/navigate/', views.StarOrderedBooks.as_view()),
]
