# Generated by Django 3.2.4 on 2022-03-27 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='staus',
            new_name='status',
        ),
    ]
