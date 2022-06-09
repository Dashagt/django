# Generated by Django 4.0.4 on 2022-05-17 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['-time_create', 'title'], 'verbose_name': 'Відомі жінки', 'verbose_name_plural': 'Відомі жінки'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='women',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='women.category', verbose_name='Категорії'),
        ),
        migrations.AlterField(
            model_name='women',
            name='content',
            field=models.TextField(blank=True, verbose_name='Текст статті'),
        ),
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публікація'),
        ),
        migrations.AlterField(
            model_name='women',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Час створення'),
        ),
        migrations.AlterField(
            model_name='women',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Час зміни'),
        ),
    ]
