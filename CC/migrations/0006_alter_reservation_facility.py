# Generated by Django 4.0.3 on 2022-04-28 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CC', '0005_remove_member_membership_type_member_membership_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='Facility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CC.facilities'),
        ),
    ]
