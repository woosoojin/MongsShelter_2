# Generated by Django 2.1.1 on 2019-07-28 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0038_auto_20190724_0905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adopting',
            old_name='description3',
            new_name='description',
        ),
        migrations.AddField(
            model_name='adopting',
            name='description2',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='adopting',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/adopting'),
        ),
        migrations.AddField(
            model_name='adopting',
            name='name2',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
