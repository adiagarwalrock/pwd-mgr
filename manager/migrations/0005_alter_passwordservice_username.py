# Generated by Django 3.2.16 on 2022-12-05 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20221205_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordservice',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.username'),
        ),
    ]
