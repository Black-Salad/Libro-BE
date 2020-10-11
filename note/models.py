from django.db import models
from django.conf import settings
from user.models import User
from bookshelf.models import Book


class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    book_id = models.ForeignKey(Book, on_delete=models.PROTECT)
    # user_id = models.IntegerField(default=0)
    # book_id = models.IntegerField(default=0)
    book_img = models.CharField(max_length=500, default="")
    book_title = models.CharField(max_length=500, default="")
    note_title = models.CharField(max_length=200)
    note_contents = models.TextField()
    note_date = models.DateTimeField(auto_now_add=True)
    note_viewcount = models.IntegerField()
    # note_like = models.IntegerField(default=0)
    note_private = models.BooleanField(default=True)
    note_state = models.BooleanField(default=True)

    class Meta:
        verbose_name: "note"
        verbose_name_plural = "notes"
        db_table = "note"
        ordering = ('-note_date',)

    def __str__(self):
        return self.note_title


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    note_id = models.ForeignKey(Note, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    user_img = models.TextField(default="")
    # note_id = models.IntegerField(default=0)
    # user_id = models.IntegerField(default=0)
    user_name = models.CharField(max_length=200, default="user.svg")
    comment_contents = models.TextField()
    # 글자수 제한 두는 게 좋을 듯
    comment_date = models.DateTimeField(auto_now_add=True, blank=True)
    comment_state = models.BooleanField(default=True)

    class Meta:
        db_table = "note_comment"
        ordering = ('comment_date',)

    def __str__(self):
        return self.comment_id


class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    # note_id = models.ForeignKey(Note, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    note_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    like_date = models.DateTimeField(auto_now_add=True, blank=True)
    # like_state = models.BooleanField(default=True)

    class Meta:
        db_table = "note_like"
        ordering = ('-like_date',)

    def __str__(self):
        return self.like_id
