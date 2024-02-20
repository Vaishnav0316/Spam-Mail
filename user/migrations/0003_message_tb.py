# Generated by Django 4.2.6 on 2024-01-05 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_register_tb_hobby_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='message_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=20)),
                ('Message', models.CharField(max_length=20)),
                ('Date', models.CharField(max_length=20)),
                ('Time', models.CharField(max_length=20)),
                ('Status', models.CharField(default='Pending', max_length=20)),
                ('FilterStatus', models.CharField(default='Pending', max_length=20)),
                ('Receiverid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.register_tb')),
                ('Senderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Senderid', to='user.register_tb')),
            ],
        ),
    ]