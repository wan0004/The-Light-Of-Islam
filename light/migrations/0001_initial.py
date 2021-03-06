# Generated by Django 3.0.6 on 2020-06-27 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('aadhar_no', models.IntegerField(blank=True, null=True)),
                ('phone_no', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
