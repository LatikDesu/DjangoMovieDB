# Generated by Django 4.1.7 on 2023-03-15 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0002_rename_movie_short_movie_shots"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rating",
            name="movie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="movie.movie",
                verbose_name="фильм",
            ),
        ),
    ]
