# Generated by Django 3.2.4 on 2022-03-27 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='staus',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out of delivery', 'Out fot delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
