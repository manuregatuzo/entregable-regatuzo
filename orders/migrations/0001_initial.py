# Generated by Django 4.1.4 on 2023-01-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], max_length=4)),
            ],
        ),
    ]
