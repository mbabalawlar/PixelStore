# Generated by Django 3.1.2 on 2021-12-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelstore', '0006_auto_20211214_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallets',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.DeleteModel(
            name='Balance',
        ),
    ]
