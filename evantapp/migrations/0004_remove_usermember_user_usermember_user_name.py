# Generated by Django 4.0.5 on 2022-06-09 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evantapp', '0003_remove_usermember_user_food'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermember',
            name='user',
        ),
        migrations.AddField(
            model_name='usermember',
            name='user_name',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]