# Generated by Django 4.0.5 on 2022-06-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_indexback_remove_indexpage_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='IndexBack',
        ),
        migrations.DeleteModel(
            name='IndexPageSlayder',
        ),
        migrations.AlterModelOptions(
            name='indexpage',
            options={'verbose_name': 'Home', 'verbose_name_plural': 'Homes'},
        ),
        migrations.RemoveField(
            model_name='indexpage',
            name='name',
        ),
        migrations.RemoveField(
            model_name='indexpage',
            name='phoneNumber',
        ),
        migrations.AddField(
            model_name='indexpage',
            name='img1',
            field=models.ImageField(null=True, upload_to='media', verbose_name='HomePage img1'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='img2',
            field=models.ImageField(null=True, upload_to='media', verbose_name='HomePage img2'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='img3',
            field=models.ImageField(null=True, upload_to='media', verbose_name='HomePage img3'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='name1',
            field=models.CharField(max_length=50, null=True, verbose_name='HomePage name1'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='name2',
            field=models.CharField(max_length=60, null=True, verbose_name='HomePage name2'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='name3',
            field=models.CharField(max_length=70, null=True, verbose_name='HomePage name3'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='number',
            field=models.CharField(max_length=30, null=True, verbose_name='HomePage number'),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='about',
            field=models.TextField(null=True, verbose_name='HomePage about'),
        ),
    ]
