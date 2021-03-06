# Generated by Django 3.1.6 on 2021-03-01 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lands', '0002_feed_leases'),
    ]

    operations = [
        migrations.CreateModel(
            name='feeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField(default='head')),
                ('body', models.TextField(default='body')),
                ('new', models.TextField(default='more')),
            ],
        ),
        migrations.DeleteModel(
            name='feed',
        ),
        migrations.AddField(
            model_name='stands',
            name='feedBody',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='stands',
            name='feedHead',
            field=models.TextField(default='No new yet'),
        ),
    ]
