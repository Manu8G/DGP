# Generated by Django 4.1.1 on 2022-12-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnogurus', '0003_alter_usuario_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(max_length=10),
        ),
    ]