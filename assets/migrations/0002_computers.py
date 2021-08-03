# Generated by Django 3.2.6 on 2021-08-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('brand', models.CharField(choices=[('Hp', 'Hp'), ('Del', 'Del'), ('Toshiba', 'Toshiba')], max_length=20)),
                ('memory', models.CharField(choices=[('500 Gb', '500 Gb'), ('1 Tb', '1 Tb')], max_length=15)),
                ('preprosser', models.CharField(choices=[('Core i3', 'Core i3'), ('Core i5', 'Core i5'), ('Core i7', 'Core i7')], max_length=15)),
            ],
        ),
    ]
