# Generated by Django 4.0.6 on 2022-07-19 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicemgmt', '0014_rename_item_exceldataimport_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exceldataimport',
            name='Company_Name',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Company_Name'),
        ),
        migrations.AlterField(
            model_name='exceldataimport',
            name='Contact_Name',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Contact_Name'),
        ),
    ]
