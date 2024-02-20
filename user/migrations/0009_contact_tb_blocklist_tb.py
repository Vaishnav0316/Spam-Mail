# Generated by Django 4.2.6 on 2024-01-12 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_contact_tb_contactid_remove_contact_tb_userid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Date', models.CharField(max_length=20)),
                ('Time', models.CharField(max_length=20)),
                ('Remarks', models.CharField(max_length=20)),
                ('Contactid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.register_tb')),
                ('Userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Userid', to='user.register_tb')),
            ],
        ),
        migrations.CreateModel(
            name='Blocklist_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Date', models.CharField(max_length=20)),
                ('Time', models.CharField(max_length=20)),
                ('Remarks', models.CharField(max_length=20)),
                ('Contactid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Contactid', to='user.register_tb')),
                ('Userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.register_tb')),
            ],
        ),
    ]
