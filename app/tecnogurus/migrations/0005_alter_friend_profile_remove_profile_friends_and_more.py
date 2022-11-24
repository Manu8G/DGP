# Generated by Django 4.1.1 on 2022-11-24 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tecnogurus', '0004_profile_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tecnogurus.profile'),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_friends', to='tecnogurus.friend'),
        ),
    ]
