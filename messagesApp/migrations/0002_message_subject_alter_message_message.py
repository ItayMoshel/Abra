# Generated by Django 4.1.4 on 2022-12-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=2000),
        ),
    ]
