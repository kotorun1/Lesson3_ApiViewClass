# Generated by Django 4.1.5 on 2023-03-09 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year_of_birth', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Yaroslav.director')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('films', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Yaroslav.film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(to='Yaroslav.genre'),
        ),
        migrations.AddField(
            model_name='film',
            name='posters',
            field=models.ManyToManyField(to='Yaroslav.poster'),
        ),
    ]
