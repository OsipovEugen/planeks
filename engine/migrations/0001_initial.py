# Generated by Django 4.1.7 on 2023-03-12 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_name', models.CharField(max_length=30, verbose_name='Column name')),
                ('data_type', models.CharField(choices=[('1', 'Full name'), ('2', 'Job'), ('3', 'Email'), ('4', 'Domain name'), ('5', 'Phone number'), ('6', 'Company name'), ('7', 'Text'), ('8', 'Integer'), ('9', 'Address'), ('10', 'Date')], default='Choose...', max_length=30, verbose_name='Type')),
                ('order', models.IntegerField(default='0')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('schema_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.schema', to_field='name')),
            ],
        ),
    ]
