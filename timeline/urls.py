from django.urls import path
from timeline import views

app_name = 'bookshelf'
urlpatterns = [
    path('', views.TimelineList.as_view()),
    path('<int:pk>/', views.TimelineDetail.as_view()),
    path('shelf', views.TimelineShelfJoinList.as_view()),
    path('star', views.TimelineStarJoinList.as_view()),
]
