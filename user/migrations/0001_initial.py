# Generated by Django 4.2.6 on 2024-01-02 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='country_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='state_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=20)),
                ('Country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country_tb')),
            ],
        ),
    ]
