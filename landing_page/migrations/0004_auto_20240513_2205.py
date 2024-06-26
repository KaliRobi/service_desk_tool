# Generated by Django 3.0 on 2024-05-13 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0003_auto_20240513_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='tilemodel',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tilemodel',
            name='title',
            field=models.CharField(default='tool name', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tilemodel',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='tilemodel',
            name='url_link',
            field=models.URLField(null=True),
        ),
    ]
