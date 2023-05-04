# Generated by Django 4.1.7 on 2023-04-04 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField()),
                ('Category', models.CharField(choices=[('SP', 'Smart Phone'), ('LT', 'Leptop'), ('SW', 'Smart Watch'), ('EP', 'EarPods'), ('PB', 'Power Bank'), ('DP', 'Mini Digital Projector'), ('HC', 'Hardcover Case'), ('MF', 'Mini foldable Fan')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
