# Generated by Django 3.2.1 on 2021-08-12 10:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productsapp', '0011_auto_20210812_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing_address',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='billing_address',
            name='user',
            field=models.ForeignKey(default=datetime.datetime(2021, 8, 12, 10, 52, 12, 617140, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(default=datetime.datetime(2021, 8, 12, 10, 52, 20, 80004, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
