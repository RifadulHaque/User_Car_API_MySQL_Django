# Generated by Django 4.1 on 2023-04-06 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_alter_user_email_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='userApp.user'),
        ),
    ]
