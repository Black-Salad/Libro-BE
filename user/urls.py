from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
    # path('shelf/', views.UserShelf.as_view()),
]
