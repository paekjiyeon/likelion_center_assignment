# Generated by Django 2.2.1 on 2019-07-23 19:09

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190724_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='media/images/'),
        ),
    ]
