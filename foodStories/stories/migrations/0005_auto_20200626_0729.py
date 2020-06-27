# Generated by Django 3.0.6 on 2020-06-26 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20200626_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='stories.Story', verbose_name='Category'),
        ),
    ]
