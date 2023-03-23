# Generated by Django 4.1.7 on 2023-03-22 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='workers',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='workers', to='developers.companyuser'),
        ),
    ]