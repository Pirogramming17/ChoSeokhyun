# Generated by Django 4.0.6 on 2022-07-15 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_alter_review_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='order',
        ),
    ]