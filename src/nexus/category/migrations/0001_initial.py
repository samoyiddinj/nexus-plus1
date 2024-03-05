# Generated by Django 5.0.2 on 2024-02-08 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('icon', models.CharField(blank=True, max_length=40, null=True)),
                ('main_icon', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('sorting', models.SmallIntegerField(null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]