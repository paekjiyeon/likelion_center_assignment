# Generated by Django 2.2.3 on 2019-07-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
