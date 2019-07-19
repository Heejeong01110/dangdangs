# Generated by Django 2.2.3 on 2019-07-19 10:21

from django.db import migrations, models
import django.db.models.deletion


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
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='image',
            field=models.FileField(default='C:\\Github\\dangdangs\\media\\images\\default', upload_to='board/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=10)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Board')),
            ],
        ),
    ]
