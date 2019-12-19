# Generated by Django 3.0 on 2019-12-15 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0002_auto_20191215_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='testimonial_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
