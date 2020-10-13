from django.db import models
from django.conf import settings
from user.models import User, Follow
from bookshelf.models import Shelf, BookStar
from note.models import Note, Like
import datetime


class Timeline(models.Model):
    timeline_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # [tl_kind]  1: 책꽂이 등록(읽기), 2: 완독, 3: 관심책 추가, 4: 독서록 등록, 5: 좋아요, 6: 팔로우
    tl_kind = models.CharField(max_length=1)
    shelf_id = models.ForeignKey(Shelf, on_delete=models.CASCADE, null=True)
    star_id = models.ForeignKey(BookStar, on_delete=models.CASCADE, null=True)
    note_id = models.ForeignKey(Note, on_delete=models.CASCADE, null=True)
    like_id = models.ForeignKey(Like, on_delete=models.CASCADE, null=True)
    follow_id = models.ForeignKey(Follow, on_delete=models.CASCADE, null=True)
    tl_state = models.BooleanField(default=True)
    tl_add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.user_id.user_name, tl_kind)

    class Meta:
        db_table = "timeline"
        ordering = ('-tl_add_date',)
