# Generated by Django 2.1.5 on 2019-03-31 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_weather_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='city',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='api.City'),
            preserve_default=False,
        ),
    ]
