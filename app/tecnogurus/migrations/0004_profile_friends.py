# Generated by Django 4.1.1 on 2022-11-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnogurus', '0003_remove_profile_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(null=True, related_name='my_friends', to='tecnogurus.friend'),
        ),
    ]
