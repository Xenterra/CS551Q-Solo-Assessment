# Generated by Django 3.1.3 on 2022-04-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gameDetails',
            fields=[
                ('uniqueid', models.IntegerField(primary_key=True, serialize=False)),
                ('gameID', models.IntegerField()),
                ('appURL', models.CharField(max_length=1000)),
                ('subtitle', models.CharField(max_length=50)),
                ('iconURL', models.CharField(max_length=1000)),
                ('averageUserRating', models.CharField(max_length=3)),
                ('numberOfRating', models.IntegerField()),
                ('inAppPurchases', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=1000)),
                ('developer', models.CharField(max_length=30)),
                ('languages', models.CharField(max_length=30)),
                ('size', models.IntegerField()),
                ('genres', models.CharField(max_length=30)),
                ('originalReleaseDate', models.DateField()),
                ('CurrentVersionReleaseDate', models.DateField()),
            ],
            options={
                'db_table': 'gamedetails',
            },
        ),
        migrations.CreateModel(
            name='gameList',
            fields=[
                ('gameID', models.IntegerField(primary_key=True, serialize=False)),
                ('gameName', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('ageRating', models.CharField(max_length=4)),
                ('primaryGenre', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'gamelist',
            },
        ),
    ]