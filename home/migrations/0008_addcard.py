# Generated by Django 4.1.5 on 2023-04-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='addcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('image', models.TextField()),
                ('price', models.CharField(max_length=122)),
                ('disc1', models.TextField()),
                ('disc2', models.TextField()),
            ],
        ),
    ]