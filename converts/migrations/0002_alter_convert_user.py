# Generated by Django 4.0.4 on 2022-05-04 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('converts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convert',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='converts', to=settings.AUTH_USER_MODEL),
        ),
    ]
