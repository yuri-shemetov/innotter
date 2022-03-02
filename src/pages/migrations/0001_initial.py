# Generated by Django 4.0.2 on 2022-03-02 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('uuid', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField()),
                ('image', models.URLField(blank=True, null=True)),
                ('is_private', models.BooleanField(default=False)),
                ('unblock_date', models.DateTimeField(blank=True, null=True)),
                ('follow_requests', models.ManyToManyField(related_name='requests', to=settings.AUTH_USER_MODEL)),
                ('followers', models.ManyToManyField(related_name='follows', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
