# Generated by Django 5.1.1 on 2024-09-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('phoneNo', models.CharField(max_length=15)),
                ('hno', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('companyName', models.CharField(max_length=100)),
                ('fromDate', models.CharField(max_length=10)),
                ('toDate', models.CharField(max_length=10)),
                ('address', models.CharField(default='Unknown address', max_length=255)),
                ('qualificationName', models.CharField(max_length=100)),
                ('percentage', models.FloatField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
