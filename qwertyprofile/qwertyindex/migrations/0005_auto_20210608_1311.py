# Generated by Django 3.2.4 on 2021-06-08 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qwertyindex', '0004_auto_20210608_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qwertyindex',
            name='github_project_url',
            field=models.URLField(max_length=300),
        ),
        migrations.AlterField(
            model_name='qwertyindex',
            name='github_url',
            field=models.URLField(),
        ),
    ]
