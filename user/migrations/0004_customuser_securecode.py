# Generated by Django 3.2.3 on 2022-08-21 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customuser_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='SecureCode',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
