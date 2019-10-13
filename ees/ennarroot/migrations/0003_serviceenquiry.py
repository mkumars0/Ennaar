# Generated by Django 2.2.5 on 2019-10-13 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ennarroot', '0002_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceEnquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(default='', max_length=500)),
                ('company_name', models.CharField(default='', max_length=500)),
                ('marker_number', models.CharField(default='', max_length=500)),
                ('date', models.CharField(default='', max_length=500)),
                ('contact_persion', models.CharField(default='', max_length=500)),
                ('mobilenumber', models.CharField(default='', max_length=500)),
                ('email', models.CharField(default='', max_length=500)),
                ('address', models.CharField(default='', max_length=500)),
                ('problem', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
