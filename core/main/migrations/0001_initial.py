# Generated by Django 4.0.5 on 2022-06-26 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Header')),
                ('about', models.CharField(max_length=50, verbose_name='About Template')),
                ('phoneNumber', models.CharField(max_length=50, verbose_name='Phone nomber')),
                ('img', models.ImageField(upload_to='media', verbose_name='Shoose imagr')),
            ],
            options={
                'verbose_name': 'IndexPage',
                'verbose_name_plural': 'IndexPages',
            },
        ),
        migrations.CreateModel(
            name='IndexPageSlayder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slayderWorlds', models.CharField(max_length=50, verbose_name='Header')),
            ],
            options={
                'verbose_name': 'IndexPageSlayder',
                'verbose_name_plural': 'IndexPageSlayders',
            },
        ),
    ]