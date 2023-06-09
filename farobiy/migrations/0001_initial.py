# Generated by Django 4.2.1 on 2023-05-18 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='MessageFromUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'MessageFromUser',
                'verbose_name_plural': 'MessageFromUsers',
            },
        ),
        migrations.CreateModel(
            name='Skils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Skil',
                'verbose_name_plural': 'Skils',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='media/farobiy/teachers')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farobiy.category')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('image', models.ImageField(upload_to='media/farobiy/courses')),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='media/farobiy/courses')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='media/farobiy/courses')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farobiy.category')),
                ('skils', models.ManyToManyField(to='farobiy.skils')),
                ('teacher', models.ManyToManyField(to='farobiy.teachers')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
    ]
