# Generated by Django 4.1.1 on 2022-10-10 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dormapp', '0003_auto_20221005_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='dormroomphoto',
            name='dateCreated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dormroomreview',
            name='dateCreated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='reshallphoto',
            name='dateCreated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='reshallreview',
            name='dateCreated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
