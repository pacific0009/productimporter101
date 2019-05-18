# Generated by Django 2.2.1 on 2019-05-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SKU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('sku', models.CharField(max_length=250, unique=True)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]