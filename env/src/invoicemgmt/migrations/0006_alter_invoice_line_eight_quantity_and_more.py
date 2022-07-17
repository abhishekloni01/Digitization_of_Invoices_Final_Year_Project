# Generated by Django 4.0.6 on 2022-07-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicemgmt', '0005_alter_invoice_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='line_eight_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_eight_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_eight_unit_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Unit Price (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_five_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_five_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_five_unit_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Unit Price (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_four_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_four_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_four_unit_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Unit Price (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_nine',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Line 9'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_nine_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_nine_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_nine_unit_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Unit Price (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_one_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_one_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_one_unit_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Unit Price (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_seven_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_seven_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_seven_unit_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Unit Price (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_six_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_six_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_six_unit_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Unit Price (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_ten_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_ten_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_ten_unit_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Unit Price (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_three_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_three_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_three_unit_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Unit Price (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two_total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two_unit_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Unit Price (D)'),
        ),
    ]