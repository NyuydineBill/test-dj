# Generated by Django 4.2.6 on 2023-10-24 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emissions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Date_Created', models.DateField(auto_now=True)),
                ('Accounting_Period', models.CharField(max_length=150)),
                ('Scope_1', models.IntegerField(null=True)),
                ('Scope_2', models.IntegerField(null=True)),
                ('Scope_3', models.IntegerField(null=True)),
            ],
        ),
    ]