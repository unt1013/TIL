# Generated by Django 2.2.5 on 2020-02-06 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='departmentStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ds_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('store_time', models.CharField(max_length=255)),
                ('phone_num', models.CharField(max_length=255)),
                ('ds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.departmentStore')),
            ],
        ),
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=255)),
                ('brand_theme', models.CharField(max_length=255)),
                ('floor', models.CharField(max_length=50)),
                ('ds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.departmentStore')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.store')),
            ],
        ),
    ]
