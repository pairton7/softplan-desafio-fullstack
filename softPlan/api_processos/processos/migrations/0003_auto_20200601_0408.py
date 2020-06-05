# Generated by Django 3.0.6 on 2020-06-01 04:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('processos', '0002_auto_20200601_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='finalizadores',
            field=models.ManyToManyField(blank=True, related_name='processos', to=settings.AUTH_USER_MODEL, verbose_name='Finalizadores'),
        ),
    ]
