# Generated by Django 3.2.1 on 2021-07-26 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0002_product1'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specification',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]