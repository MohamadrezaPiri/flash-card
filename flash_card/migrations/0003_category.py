# Generated by Django 4.1.7 on 2023-03-13 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flash_card', '0002_flashcard_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
