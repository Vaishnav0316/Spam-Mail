# Generated by Django 4.2.6 on 2024-01-24 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site_admin', '0006_seasoncountry_tb'),
        ('user', '0010_customerhobby_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customeragefactor_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Factorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.agefactor_tb')),
                ('Userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.register_tb')),
            ],
        ),
    ]