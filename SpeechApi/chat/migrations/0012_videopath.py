# Generated by Django 3.1.4 on 2023-05-06 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_auto_20230505_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videpath', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
