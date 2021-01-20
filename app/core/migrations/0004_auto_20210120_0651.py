# Generated by Django 3.1.5 on 2021-01-20 06:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20210120_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('user', 'name')},
        ),
    ]
