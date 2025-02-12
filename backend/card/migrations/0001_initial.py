# Generated by Django 5.1.6 on 2025-02-12 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('element', '0002_rename_atmic_mass_element_atomic_mass_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementCard',
            fields=[
                ('element_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='element.element')),
                ('type', models.CharField(max_length=10, verbose_name='カードタイプ')),
                ('name', models.CharField(max_length=30, verbose_name='カード名')),
                ('cost', models.IntegerField(verbose_name='コスト')),
            ],
            options={
                'abstract': False,
            },
            bases=('element.element', models.Model),
        ),
        migrations.CreateModel(
            name='ToolCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, verbose_name='カードタイプ')),
                ('name', models.CharField(max_length=30, verbose_name='カード名')),
                ('cost', models.IntegerField(verbose_name='コスト')),
                ('effect', models.TextField(max_length=200, verbose_name='効果')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='説明')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompoundCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, verbose_name='カードタイプ')),
                ('name', models.CharField(max_length=30, verbose_name='カード名')),
                ('cost', models.IntegerField(verbose_name='コスト')),
                ('atomic_mass', models.FloatField(verbose_name='原子量')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='説明')),
                ('elements', models.ManyToManyField(to='card.elementcard', verbose_name='構成元素')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
