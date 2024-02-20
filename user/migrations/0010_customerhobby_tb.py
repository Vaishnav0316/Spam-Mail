# Generated by Django 4.2.6 on 2024-01-14 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site_admin', '0005_agefactor_tb'),
        ('user', '0009_contact_tb_blocklist_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customerhobby_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Factorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.hobbyfactor_tb')),
                ('Hobbyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.hobbyname_tb')),
                ('Userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.register_tb')),
            ],
        ),
    ]
