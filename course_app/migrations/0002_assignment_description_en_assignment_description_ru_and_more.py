# Generated by Django 5.1.5 on 2025-01-19 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_en',
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_ru',
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_name_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_name_ru',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='coursereview',
            name='comment_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coursereview',
            name='comment_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='option',
            name='test_en',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='option',
            name='test_ru',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='option',
            name='text_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='option',
            name='text_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_ru',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='teacherreview',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='teacherreview',
            name='text_ru',
            field=models.TextField(null=True),
        ),
    ]
