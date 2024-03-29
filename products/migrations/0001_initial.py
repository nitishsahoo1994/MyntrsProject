# Generated by Django 2.2.3 on 2019-12-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=29.99, max_digits=100)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
                ('slug', models.SlugField(max_length=64, unique_for_date='added')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-added',),
            },
        ),
    ]
