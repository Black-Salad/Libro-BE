from django.db import models
from django.conf import settings


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=200)
    user_pw = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    user_introduction = models.TextField()
    user_crea_date = models.DateTimeField(auto_now_add=True, blank=True)
    user_state = models.BooleanField(default=True)

    class Meta:
        db_table = "user"
        ordering = ('-user_crea_date',)

    def __str__(self):
        return str(self.user_id)


class Follow(models.Model):
    follow_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following")
    target_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followed")
    follow_dt = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = "follow"
        ordering = ('-follow_dt',)

    def __str__(self):
        return self.follow_id
