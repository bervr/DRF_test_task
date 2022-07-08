# Generated by Django 4.0.5 on 2022-07-07 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_number', models.IntegerField(primary_key=True, serialize=False)),
                ('game_name', models.CharField(max_length=64, verbose_name='название игры')),
                ('game_go', models.BooleanField(default=False)),
                ('game_start', models.DateTimeField(blank=True, null=True)),
                ('game_finish', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GameLevel',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('geo_lat', models.FloatField(max_length=16, verbose_name='широта')),
                ('geo_lng', models.FloatField(max_length=16, verbose_name='долгота')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='название уровня')),
                ('task', models.TextField(verbose_name='текст задания')),
                ('answer', models.CharField(max_length=256)),
                ('level_active', models.BooleanField(default=True)),
                ('level_of_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_id', to='api.game', verbose_name='игра')),
            ],
        ),
        migrations.AlterModelTable(
            name='gamesummary',
            table='base_stat',
        ),
        migrations.CreateModel(
            name='TeamAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answ_for_game', to='api.game', verbose_name='игра')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='api.gamelevel', verbose_name='уровень')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_team', to=settings.AUTH_USER_MODEL, verbose_name='команда')),
            ],
        ),
        migrations.CreateModel(
            name='Promt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promt1', models.CharField(db_index=True, max_length=300)),
                ('promt2', models.CharField(db_index=True, max_length=300)),
                ('promt3', models.CharField(db_index=True, max_length=300)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promts', to='api.gamelevel', verbose_name='уровень')),
            ],
        ),
        migrations.CreateModel(
            name='GamePlay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_started', models.DateTimeField(blank=True, null=True)),
                ('level_finished', models.DateTimeField(blank=True, null=True)),
                ('level_status', models.CharField(choices=[('DN', 'сдано'), ('TTA', 'неверный ответ'), ('NSD', 'не начато')], default='NSD', max_length=3, verbose_name='статус')),
                ('getted_promt_counter', models.PositiveIntegerField(default=0)),
                ('data', models.JSONField(default={1: False, 2: False, 3: False})),
                ('wrong_counter_answer', models.PositiveIntegerField(default=0)),
                ('level_penalty', models.DecimalField(decimal_places=11, max_digits=17, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.game', verbose_name='игра')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_level', to='api.gamelevel', verbose_name='уровень')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playing_team', to=settings.AUTH_USER_MODEL, verbose_name='команда')),
            ],
        ),
    ]