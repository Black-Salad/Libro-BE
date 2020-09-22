from django.urls import path
from bookshelf import views

app_name = 'bookshelf'
urlpatterns = [
    path("shelf/", views.ShelfList.as_view()),
    # path(""),
]
