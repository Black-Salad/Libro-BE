from django.db import models
from django.conf import settings
from user.models import User
import datetime


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=200, default="")
    book_author = models.CharField(max_length=200, default="")
    book_publisher = models.CharField(max_length=200, default="")
    book_img = models.CharField(max_length=500, default="")  # 책 thumbnail 이미지
    book_desc = models.TextField()  # 책 description
    book_url = models.CharField(max_length=500, default="")  # 책 상세 url
    book_isbn = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.book_title

    class Meta:
        db_table = "book_info"
        # ordering = ('-book_id',)


class Shelf(models.Model):
    shelf_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.PROTECT)
    shelf_state = models.CharField(max_length=1)
    start_date = models.DateField(null=False, default=datetime.date.today)
    end_date = models.DateField()  # default 지정 필요 (9999년)
    shelf_add_date = models.DateTimeField(auto_now_add=True)  # 책꽂이에 추가한 일시

    class Meta:
        db_table = "book_shelf"
        ordering = ('-shelf_add_date',)

    def __str__(self):
        return '{}의 책 {}'.format(self.user_id.user_name, self.book_id.book_title)


class BookStar(models.Model):
    star_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.PROTECT)
    star_add_date = models.DateTimeField(auto_now_add=True)  # 관심책에 추가한 일시

    class Meta:
        db_table = "book_star"
        ordering = ('-star_add_date',)

    def __str__(self):
        return '{}의 책 {}'.format(self.user_id.user_name, self.book_id.book_title)
