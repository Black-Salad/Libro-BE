# Generated by Django 3.1 on 2020-10-11 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_email', models.CharField(max_length=200)),
                ('user_pw', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
                ('user_img', models.FileField(default='user.svg', upload_to='')),
                ('user_introduction', models.TextField(default='')),
                ('user_crea_date', models.DateTimeField(auto_now_add=True)),
                ('user_state', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'user',
                'ordering': ('-user_crea_date',),
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('follow_id', models.AutoField(primary_key=True, serialize=False)),
                ('follow_dt', models.DateTimeField(auto_now_add=True)),
                ('target_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to='user.user')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='user.user')),
            ],
            options={
                'db_table': 'follow',
                'ordering': ('-follow_dt',),
            },
        ),
    ]
