# Generated by Django 5.0.6 on 2024-05-27 10:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('travelers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('notification_status', models.CharField(max_length=200, verbose_name='Notification Status')),
                ('last_updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('registered_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_registered_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('notification_content', models.TextField()),
                ('notification_date', models.DateField()),
                ('last_updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('registered_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_registered_by', to=settings.AUTH_USER_MODEL)),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='travelers.travelerrecord')),
                ('notification_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='notifications.notificationstatus')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
