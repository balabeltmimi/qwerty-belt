# Generated by Django 3.2.4 on 2021-06-08 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qwertyindex', '0002_auto_20210607_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscibemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'email',
                'verbose_name_plural': 'email',
            },
        ),
    ]
