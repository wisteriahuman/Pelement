# Generated by Django 5.1.6 on 2025-02-11 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=3, verbose_name='元素記号')),
                ('number', models.IntegerField(verbose_name='元素番号')),
                ('atmic_mass', models.FloatField(verbose_name='原子量')),
                ('period', models.IntegerField(verbose_name='周期')),
                ('family', models.IntegerField(verbose_name='族')),
                ('properties', models.CharField(max_length=30, verbose_name='性質')),
                ('description', models.TextField(max_length=200, verbose_name='説明')),
                ('image', models.ImageField(blank=True, null=True, upload_to='element/image/', verbose_name='画像')),
            ],
        ),
    ]
