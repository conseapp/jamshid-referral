# Generated by Django 5.0.1 on 2024-01-12 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referral',
            old_name='active',
            new_name='used',
        ),
    ]
