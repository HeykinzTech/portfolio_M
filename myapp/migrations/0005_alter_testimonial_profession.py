# Generated by Django 4.1.7 on 2023-04-02 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_testimonial_alter_member_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='profession',
            field=models.CharField(max_length=50),
        ),
    ]