# Generated by Django 3.2.2 on 2021-05-28 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_conseiller_use'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='use',
            name='idC',
        ),
        migrations.DeleteModel(
            name='Conseiller',
        ),
    ]
