# Generated by Django 2.0.2 on 2018-04-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatson', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='facecluster',
            name='silhouette_score',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
