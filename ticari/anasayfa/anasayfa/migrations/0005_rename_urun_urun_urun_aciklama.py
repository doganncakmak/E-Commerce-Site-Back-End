# Generated by Django 3.2.13 on 2022-05-20 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0004_urun_urun'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urun',
            old_name='urun',
            new_name='urun_aciklama',
        ),
    ]
