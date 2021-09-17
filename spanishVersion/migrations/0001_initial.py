# Generated by Django 3.2.6 on 2021-09-17 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Secretary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secretary', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=280)),
                ('presentation', models.TextField()),
                ('secretary_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adminResp', to='spanishVersion.secretary')),
            ],
        ),
    ]
