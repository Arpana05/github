# Generated by Django 5.0.6 on 2024-07-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custompermission',
            name='role',
        ),
        migrations.AddField(
            model_name='customrole',
            name='permissions',
            field=models.ManyToManyField(blank=True, related_name='roles', to='users.custompermission'),
        ),
    ]
