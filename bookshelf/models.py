from django.db import models
from django.conf import settings
from user.models import User
import datetime


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=200, default="")
    book_author = models.CharField(max_length=200, default="")
    book_publisher = models.CharField(
        max_length=200, default="", null=True, blank=True)
    book_img = models.CharField(
        max_length=500, default="", null=True, blank=True)  # 책 thumbnail 이미지
    book_desc = models.TextField(null=True, blank=True)  # 책 description
    book_url = models.CharField(max_length=500, default="")  # 책 상세 url
    book_isbn = models.CharField(max_length=500, default="")
    book_star_cnt = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{} {}'.format(self.book_title, self.book_id)

    class Meta:
        db_table = "book_info"
        # ordering = ('-book_id',)


class Shelf(models.Model):
    shelf_id = models.AutoField(primary_key=True)  # is this necessary?
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(
        Book, on_delete=models.PROTECT)  # is this necessary?
    book_isbn = models.CharField(max_length=100)
    shelf_state = models.CharField(max_length=1)
    start_date = models.DateField(null=False, default=datetime.date.today)
    end_date = models.DateField(default="9999-12-31")  # default 지정 필요 (9999년)
    shelf_add_date = models.DateTimeField(auto_now_add=True)  # 책꽂이에 추가한 일시

    class Meta:
        db_table = "book_shelf"
        ordering = ('-shelf_add_date',)

    def __str__(self):
        # self.user_id.user_name+" "+self.book_id.book_title
        return '{} {} {}'.format(self.shelf_id, self.user_id.user_name, self.book_id.book_title)


class BookStar(models.Model):
    star_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(
        Book, on_delete=models.PROTECT)  # is this necessary?
    book_isbn = models.CharField(max_length=100)
    star_add_date = models.DateTimeField(auto_now_add=True)  # 관심책에 추가한 일시

    class Meta:
        db_table = "book_star"
        ordering = ('-star_add_date',)

    def __str__(self):
        # self.user_id.user_name+" "+self.book_id.book_title
        return '{} {} {}'.format(self.star_id, self.user_id.user_name, self.book_id.book_title)
        # 'Asentamiento: {} {} {} {} {} '.format(self.id_asentamiento, self.nom_asentamiento, self.tipo_centro, self.nom_centro, self.num_local)
