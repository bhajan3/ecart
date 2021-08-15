# Generated by Django 3.2.1 on 2021-08-05 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customerapp', '0006_auto_20210804_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cus_review',
            old_name='reviews',
            new_name='review',
        ),
        migrations.AlterField(
            model_name='cus_review',
            name='star',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cus_review',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
