# Generated by Django 3.1.7 on 2021-04-15 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    # initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nipguru', models.IntegerField()),
                ('kelaminguru', models.BooleanField()),
                ('namaguru', models.CharField(max_length=100)),
                ('alamatguru', models.TextField()),
                ('hpguru', models.CharField(max_length=15)),
                ('photoguru', models.CharField(max_length=100)),
                ('jenjang', models.CharField(max_length=50)),
                ('jurusan', models.CharField(max_length=50)),
            ],
        ),
    ]
