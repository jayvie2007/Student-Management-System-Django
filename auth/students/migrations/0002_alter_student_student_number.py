# Generated by Django 4.1.7 on 2023-04-12 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_number',
            field=models.CharField(max_length=8),
        ),
    ]
