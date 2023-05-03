# Generated by Django 4.2 on 2023-04-28 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('user_pw', models.CharField(blank=True, max_length=30, null=True)),
                ('user_name', models.CharField(blank=True, max_length=30, null=True)),
                ('user_birth', models.DateField(blank=True, null=True)),
                ('user_gender', models.CharField(blank=True, max_length=2, null=True)),
                ('user_height', models.IntegerField(blank=True, null=True)),
                ('user_weight', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]