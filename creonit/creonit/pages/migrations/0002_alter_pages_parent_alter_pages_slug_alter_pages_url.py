# Generated by Django 4.2.11 on 2024-04-23 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='pages.pages'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pages',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
