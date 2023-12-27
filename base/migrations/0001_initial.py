# Generated by Django 4.2.7 on 2023-12-27 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number_of_players', models.IntegerField()),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('number_of_teams', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number_of_goals_scored', models.IntegerField()),
                ('number_of_goals_assisted', models.IntegerField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club', to='base.club')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='league', to='base.league'),
        ),
    ]
