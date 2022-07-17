# Generated by Django 4.0.6 on 2022-07-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicemgmt', '0006_alter_invoice_line_eight_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='line_eight_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_five_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_four_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_nine_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_one_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_seven_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_six_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_ten_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_three_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total (D)'),
        ),
    ]