# Generated by Django 4.1.7 on 2023-04-10 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userhome', '0002_alter_address_city_alter_userprofile_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(choices=[('Madurai', 'Madurai'), ('Banglore', 'Banglore'), ('Kannur', 'Kannur'), ('Hydrabad', 'Hydrabad'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Ernakulam', 'Ernakulam'), ('Coimbator', 'Coimbator'), ('Hubli', 'Hubli'), ('Kozhikkode', 'Kozhikkode')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='district',
            field=models.CharField(blank=True, choices=[('Madurai', 'Madurai'), ('Banglore', 'Banglore'), ('Kannur', 'Kannur'), ('Hydrabad', 'Hydrabad'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Ernakulam', 'Ernakulam'), ('Coimbator', 'Coimbator'), ('Hubli', 'Hubli'), ('Kozhikkode', 'Kozhikkode')], max_length=20, null=True),
        ),
    ]