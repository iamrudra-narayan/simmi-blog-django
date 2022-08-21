# Generated by Django 4.1 on 2022-08-21 15:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=30)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('description', models.TextField(max_length=30)),
                ('image_file', models.FileField(default='', upload_to='media/pics/')),
            ],
        ),
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.TextField(max_length=30)),
                ('email', models.EmailField(default='', max_length=30)),
                ('password', models.TextField(max_length=30)),
                ('date', models.DateField(verbose_name=django.utils.timezone.now)),
            ],
        ),
    ]