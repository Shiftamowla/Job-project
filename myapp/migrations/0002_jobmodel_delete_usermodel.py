# Generated by Django 5.1 on 2024-09-02 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('selary', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('logopic', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='usermodel',
        ),
    ]
