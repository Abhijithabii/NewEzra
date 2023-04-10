# Generated by Django 4.1.7 on 2023-04-10 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(null=True, upload_to='category')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.PositiveBigIntegerField(null=True)),
                ('updated', models.DateField(auto_now=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminhome.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVarient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('varientname', models.CharField(max_length=100, null=True)),
                ('varstock', models.PositiveIntegerField(null=True)),
                ('proname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='adminhome.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(null=True, upload_to='media')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminhome.product')),
            ],
        ),
    ]
