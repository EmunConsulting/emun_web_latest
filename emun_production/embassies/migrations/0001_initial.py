# Generated by Django 5.0.6 on 2024-05-27 10:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Embassy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('embassy_id', models.CharField(max_length=15, verbose_name='Embassy ID')),
                ('embassy_name', models.CharField(max_length=100, verbose_name='Embassy Name')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
                ('phone_number', models.CharField(blank=True, max_length=15, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('website', models.CharField(max_length=200, verbose_name='Website')),
                ('last_updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('registered_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_registered_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
