# Generated by Django 4.0.2 on 2022-03-10 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_reply_to'),
        ('likes', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_post', to='posts.post'),
        ),
    ]
