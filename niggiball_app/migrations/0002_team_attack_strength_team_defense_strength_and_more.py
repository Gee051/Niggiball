# Generated by Django 5.1.1 on 2024-09-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niggiball_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='attack_strength',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='team',
            name='defense_strength',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='team',
            name='recent_form',
            field=models.IntegerField(default=0),
        ),
    ]
