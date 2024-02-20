# Generated by Django 4.2.6 on 2024-02-05 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site_admin', '0006_seasoncountry_tb'),
        ('user', '0011_customeragefactor_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerSeasoncountry_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Factorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.seasonfactor_tb')),
                ('Userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.register_tb')),
            ],
        ),
    ]
