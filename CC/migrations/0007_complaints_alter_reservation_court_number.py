# Generated by Django 4.0.3 on 2022-04-28 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CC', '0006_alter_reservation_facility'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Telephone', models.IntegerField(max_length=20)),
                ('Complaint', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='reservation',
            name='Court_number',
            field=models.IntegerField(default=1, max_length=1),
        ),
    ]
