# Generated by Django 5.2.3 on 2025-06-13 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
