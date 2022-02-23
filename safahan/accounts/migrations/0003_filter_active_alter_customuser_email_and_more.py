# Generated by Django 4.0.2 on 2022-02-23 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_conditions_filter_permium_rank_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='active',
            field=models.BooleanField(default=1, verbose_name='boolean field'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='family name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mac_address',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='a unique address of every device'),
        ),
        migrations.CreateModel(
            name='StockScout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name of stock')),
                ('instanceCode', models.CharField(max_length=100, verbose_name='code for instance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='what user give this')),
            ],
        ),
        migrations.CreateModel(
            name='CoinScout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='what user give this')),
            ],
        ),
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name of alarm')),
                ('instanceCode', models.CharField(max_length=100, verbose_name='instance code')),
                ('type', models.IntegerField(verbose_name='type of alarm')),
                ('valueType', models.CharField(max_length=50, verbose_name='type for value')),
                ('value', models.CharField(max_length=50, verbose_name='value')),
                ('active', models.BooleanField(verbose_name='boolean field')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='what user give this')),
            ],
        ),
    ]
