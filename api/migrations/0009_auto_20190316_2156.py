# Generated by Django 2.1.5 on 2019-03-16 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190303_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='id',
        ),
        migrations.AddField(
            model_name='city',
            name='city_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]