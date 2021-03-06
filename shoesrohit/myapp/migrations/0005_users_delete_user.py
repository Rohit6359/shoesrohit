# Generated by Django 4.0.3 on 2022-03-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_user_address_remove_user_mobile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('password', models.CharField(max_length=25, null=True)),
                ('address', models.TextField(null=True)),
                ('doj', models.DateField(null=True)),
                ('pic', models.FileField(default='avtar.png', null=True, upload_to='Profile Pic')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
