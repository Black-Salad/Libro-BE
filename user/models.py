from django.db import models
from django.conf import settings


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=200)
    user_pw = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    user_introduction = models.TextField()
    user_crea_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = "user"
        ordering = ('-user_crea_date',)

    def __str__(self):
        return self.user_id


class Shelf(models.Model):
    shelf_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)
    book_id = models.IntegerField(default=0)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    shelf_state = models.CharField(max_length=1)
    shelf_startdate = models.CharField(max_length=200, blank=True)
    shelf_enddate = models.CharField(max_length=200, blank=True)
    shelf_star = models.BooleanField(default=True)

    class Meta:
        db_table = "user_shelf"
        ordering = ('-shelf_id',)

    def __str__(self):
        return self.shelf_id
