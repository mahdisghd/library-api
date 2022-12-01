# Generated by Django 3.2.16 on 2022-11-28 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=13)),
                ('quantity', models.IntegerField(default=0)),
                ('return_date', models.DateTimeField()),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.category')),
                ('person_lent_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.person')),
            ],
        ),
    ]