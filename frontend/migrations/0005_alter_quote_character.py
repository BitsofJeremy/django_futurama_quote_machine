# Generated by Django 3.2.6 on 2021-08-03 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_auto_20210802_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='character',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='frontend.character'),
        ),
    ]
