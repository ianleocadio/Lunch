# Generated by Django 2.0.6 on 2018-06-25 14:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realDate', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('spent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('day', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='app.Day')),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='month',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Year'),
        ),
        migrations.AddField(
            model_name='day',
            name='month',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Month'),
        ),
    ]
