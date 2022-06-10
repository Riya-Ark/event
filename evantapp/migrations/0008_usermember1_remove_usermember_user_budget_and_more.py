# Generated by Django 4.0.4 on 2022-06-09 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evantapp', '0007_delete_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMember1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25, unique=True)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_guest', models.IntegerField()),
                ('user_time', models.DateTimeField(max_length=255)),
                ('user_budget', models.IntegerField()),
                ('user_venue', models.CharField(max_length=255)),
                ('user_phone', models.IntegerField()),
                ('user_event', models.CharField(max_length=255)),
                ('user_discription', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='usermember',
            name='user_budget',
        ),
        migrations.RemoveField(
            model_name='usermember',
            name='user_discription',
        ),
        migrations.RemoveField(
            model_name='usermember',
            name='user_event',
        ),
        migrations.RemoveField(
            model_name='usermember',
            name='user_guest',
        ),
        migrations.RemoveField(
            model_name='usermember',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='usermember',
            name='user_phone',
        ),
        migrations.RemoveField(
            model_name='usermember',
            name='user_time',
        ),
        migrations.RemoveField(
            model_name='usermember',
            name='user_venue',
        ),
        migrations.AddField(
            model_name='usermember',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]