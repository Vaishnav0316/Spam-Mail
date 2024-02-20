# Generated by Django 4.2.6 on 2024-01-02 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site_admin', '0002_hobbyname_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='hobbyfactor_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Factorname', models.CharField(max_length=20)),
                ('Hobby_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.hobbyname_tb')),
            ],
        ),
    ]
