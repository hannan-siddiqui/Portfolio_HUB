# Generated by Django 3.2.20 on 2024-02-09 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0010_alter_student_rollno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
