# Generated by Django 4.0.3 on 2022-03-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='doj',
            field=models.DateField(null=True),
        ),
    ]