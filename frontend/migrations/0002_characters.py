# Generated by Django 3.2.6 on 2021-08-03 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('quotes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.quotes')),
            ],
        ),
    ]
