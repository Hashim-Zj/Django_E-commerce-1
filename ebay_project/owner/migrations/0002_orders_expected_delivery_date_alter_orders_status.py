# Generated by Django 5.0.7 on 2024-08-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='expected_delivery_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('dispatched', 'dispatched'), ('canceiled', 'canceiled'), ('order-placed', 'order-placed'), ('delivered', 'delivered')], default='order-placed', max_length=100),
        ),
    ]
