# Generated by Django 2.0.2 on 2018-03-26 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180326_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
