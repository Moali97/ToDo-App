# Generated by Django 3.1.7 on 2021-03-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_auto_20210205_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
    ]
