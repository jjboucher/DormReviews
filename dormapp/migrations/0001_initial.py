# Generated by Django 4.1.1 on 2022-12-02 23:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DormRoom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('roomNumber', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ResHall',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ResHallReview',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('starRating', models.IntegerField(default=0)),
                ('reviewTitle', models.CharField(max_length=255)),
                ('reviewBody', models.TextField(max_length=1500)),
                ('dateCreated', models.DateTimeField(auto_now=True)),
                ('resHall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dormapp.reshall')),
            ],
        ),
        migrations.CreateModel(
            name='ResHallPhoto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='res-hall-photos')),
                ('dateCreated', models.DateTimeField(auto_now=True)),
                ('resHall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dormapp.reshall')),
            ],
        ),
        migrations.AddField(
            model_name='reshall',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dormapp.university'),
        ),
        migrations.CreateModel(
            name='DormRoomReview',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('starRating', models.IntegerField(default=0)),
                ('reviewTitle', models.CharField(max_length=255)),
                ('reviewBody', models.TextField(max_length=1500)),
                ('dateCreated', models.DateTimeField(auto_now=True)),
                ('dormRoom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dormapp.dormroom')),
            ],
        ),
        migrations.CreateModel(
            name='DormRoomPhoto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='dorm-room-photos')),
                ('dateCreated', models.DateTimeField(auto_now=True)),
                ('dormRoom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dormapp.dormroom')),
            ],
        ),
        migrations.AddField(
            model_name='dormroom',
            name='resHall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dormapp.reshall'),
        ),
    ]
