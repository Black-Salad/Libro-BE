from django.db import models
from django.conf import settings
# from note.models import Note


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=200)
    user_pw = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    user_img = models.FileField(default="user.svg")
    user_introduction = models.TextField(default="")
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
    follow_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = "follow"
        ordering = ('-follow_date',)

    def __str__(self):
        return str(self.follow_id)


class Alarm(models.Model):
    alarm_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    target_user_id = models.IntegerField(null=False)
    # note_id = models.IntegerField(default=0)
    note_id = models.ForeignKey(
        "note.Note", on_delete=models.CASCADE, null=True)
    # https://jupiny.com/2016/10/23/models-circular-import-dependencies/
    alarm_type = models.IntegerField(default=0)
    alarm_state = models.BooleanField(default=True)
    alarm_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "alarm"
        ordering = ('-alarm_date',)

    def __str__(self):
        return self.alarm_id
