# Generated by Django 3.1.7 on 2021-04-17 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_guru_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guru',
            name='photoguru',
            field=models.CharField(default='noimage.png', max_length=100),
        ),
    ]