# Generated by Django 4.1.7 on 2023-03-25 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ('created_at',)},
        ),
        migrations.AlterField(
            model_name='member',
            name='profile_picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]