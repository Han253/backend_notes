# Generated by Django 4.2.3 on 2023-07-12 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('contenido', models.CharField(max_length=300)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
