# Generated by Django 3.2.6 on 2021-08-03 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0005_finance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.vehicle')),
            ],
        ),
    ]
