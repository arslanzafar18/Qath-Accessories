# Generated by Django 3.2.12 on 2023-02-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20230221_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Ceremonial', 'Ceremonial'), ('Women', 'Women'), ('Men', 'Men'), ('Courtwear', 'Courtwear'), ('Accessories', 'Accessories')], default='Accessories', max_length=20),
        ),
    ]
