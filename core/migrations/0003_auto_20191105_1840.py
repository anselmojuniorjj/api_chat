# Generated by Django 2.2.6 on 2019-11-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191029_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversa',
            name='conversation_id',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
