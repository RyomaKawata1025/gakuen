# Generated by Django 2.1.5 on 2020-07-05 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0009_auto_20200705_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='rec_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='match.Profile'),
        ),
    ]
