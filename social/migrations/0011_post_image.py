# Generated by Django 4.0.1 on 2022-01-30 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/post_photos'),
        ),
    ]