from django.urls import path
from note import views

app_name = 'note'
urlpatterns = [
    path('', views.NoteList.as_view()),
    path('<int:pk>/', views.NoteDetail.as_view()),
    path('search/', views.NoteListSearch.as_view()),
    path('comment/', views.NoteComment.as_view()),
    path('comment/userjoin/', views.NoteCommentUser.as_view()),
    path('comment/<int:pk>/', views.NoteCommentDetail.as_view()),
    path('like/', views.NoteLike.as_view()),
    path('like/<int:pk>/', views.NoteLikeDetail.as_view()),
    path('like/count/', views.NoteLikeJoin.as_view())
]
