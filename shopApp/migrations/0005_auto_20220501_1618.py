# Generated by Django 3.1.3 on 2022-05-01 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0004_shoppingcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='customerID',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='shoppingcart',
            table='shoppingCart',
        ),
    ]