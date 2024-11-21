# Generated by Django 3.2.12 on 2023-05-31 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Ceremonial', 'Ceremonial'), ('Women', 'Women'), ('Courtwear', 'Courtwear'), ('Men', 'Men'), ('Accessories', 'Accessories')], default='Accessories', max_length=20),
        ),
    ]
