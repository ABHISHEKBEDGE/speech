# Generated by Django 4.1.1 on 2023-04-21 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_prospectcompany_numberofinquisitionquestions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionssalesrepcompany',
            name='salesRepCompany_id',
        ),
    ]
