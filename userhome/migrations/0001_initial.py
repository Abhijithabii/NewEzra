# Generated by Django 4.1.7 on 2023-04-10 16:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner')),
                ('title', models.CharField(max_length=300, null=True)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Mobile number should only contain digits', regex='^\\d+$')])),
                ('address', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user')),
                ('district', models.CharField(blank=True, choices=[('Thiruvananthapuram', 'Thiruvananthapuram'), ('Hubli', 'Hubli'), ('Hydrabad', 'Hydrabad'), ('Kannur', 'Kannur'), ('Ernakulam', 'Ernakulam'), ('Coimbator', 'Coimbator'), ('Kozhikkode', 'Kozhikkode'), ('Banglore', 'Banglore'), ('Madurai', 'Madurai')], max_length=20, null=True)),
                ('state', models.CharField(choices=[('Kerala', 'Kerala'), ('Tamilnadu', 'Tamilnadu'), ('Karnataka', 'Karnataka'), ('AndraPradesh', 'AndraPradesh')], max_length=20, null=True)),
                ('pincode', models.PositiveIntegerField(blank=True, null=True)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_blocked', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=200)),
                ('address_line_1', models.CharField(max_length=255)),
                ('address_line_2', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Mobile number should only contain digits', regex='^\\d+$')])),
                ('city', models.CharField(choices=[('Thiruvananthapuram', 'Thiruvananthapuram'), ('Hubli', 'Hubli'), ('Hydrabad', 'Hydrabad'), ('Kannur', 'Kannur'), ('Ernakulam', 'Ernakulam'), ('Coimbator', 'Coimbator'), ('Kozhikkode', 'Kozhikkode'), ('Banglore', 'Banglore'), ('Madurai', 'Madurai')], max_length=255)),
                ('state', models.CharField(choices=[('Kerala', 'Kerala'), ('Tamilnadu', 'Tamilnadu'), ('Karnataka', 'Karnataka'), ('AndraPradesh', 'AndraPradesh')], max_length=255)),
                ('pincode', models.PositiveIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
