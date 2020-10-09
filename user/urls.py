from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
    path('<int:pk>/update/', views.UserUpdate.as_view()),
    path('follow/', views.FollowList.as_view()),
    path('follow/<int:pk>/', views.FollowDetail.as_view()),
]
