# Generated by Django 4.1 on 2023-04-07 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0006_alter_user_age_alter_user_sal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sal',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
    ]
