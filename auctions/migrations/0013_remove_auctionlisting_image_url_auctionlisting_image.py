# Generated by Django 4.2.4 on 2023-09-12 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_auctionlisting_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='image_url',
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
