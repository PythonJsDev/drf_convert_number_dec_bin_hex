# Generated by Django 4.0.4 on 2022-05-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converts', '0004_alter_convert_base'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convert',
            name='base',
        ),
        migrations.AlterField(
            model_name='convert',
            name='value_bin',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='convert',
            name='value_dec',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
