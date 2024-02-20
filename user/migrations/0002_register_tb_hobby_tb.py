# Generated by Django 4.2.6 on 2024-01-02 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site_admin', '0004_season_tb_seasonfactor_tb'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='register_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=20)),
                ('DOB', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=20)),
                ('SecurityQuestion', models.CharField(max_length=20)),
                ('Answer', models.CharField(max_length=20)),
                ('Username', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('Countryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country_tb')),
                ('Stateid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.state_tb')),
            ],
        ),
        migrations.CreateModel(
            name='hobby_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hobbyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.hobbyname_tb')),
                ('Userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.register_tb')),
            ],
        ),
    ]
