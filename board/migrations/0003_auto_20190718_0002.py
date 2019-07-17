# Generated by Django 2.2.3 on 2019-07-17 15:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20190711_0243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='like',
        ),
        migrations.RemoveField(
            model_name='board',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='board',
            name='image',
            field=models.ImageField(default='https://image.flaticon.com/icons/svg/149/149852.svg', upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]