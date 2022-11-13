# Generated by Django 4.1.2 on 2022-11-13 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Airport",
            fields=[
                ("name", models.CharField(max_length=128)),
                (
                    "iata",
                    models.TextField(max_length=5, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
            ],
            options={
                "verbose_name": "city",
                "verbose_name_plural": "cities",
            },
        ),
        migrations.CreateModel(
            name="Continent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="Hotel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("standard", models.IntegerField()),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="travels.city"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Trip",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("departure", models.DateTimeField()),
                ("arrival", models.DateTimeField()),
                ("number_of_days", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Bed & Breakfast", "Bed & Breakfast"),
                            ("Half Board", "Half Board"),
                            ("Full Board", "Full Board"),
                            ("All Inclusive", "All Inclusive"),
                        ],
                        max_length=32,
                    ),
                ),
                ("price_for_an_adult", models.IntegerField(help_text="Euro")),
                ("price_for_a_child", models.IntegerField(help_text="Euro")),
                ("promoted", models.BooleanField()),
                ("number_of_places_for_adults", models.IntegerField()),
                ("number_of_places_for_children", models.IntegerField()),
                (
                    "from_where",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trips_from",
                        to="travels.airport",
                    ),
                ),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="travels.hotel"
                    ),
                ),
                (
                    "to_where",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trips_to",
                        to="travels.airport",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                (
                    "continent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="travels.continent",
                    ),
                ),
            ],
            options={
                "verbose_name": "country",
                "verbose_name_plural": "countries",
            },
        ),
        migrations.AddField(
            model_name="city",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="travels.country"
            ),
        ),
        migrations.AddField(
            model_name="airport",
            name="city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="travels.city"
            ),
        ),
        migrations.AddConstraint(
            model_name="hotel",
            constraint=models.CheckConstraint(
                check=models.Q(("standard__gte", 1), ("standard__lte", 5)),
                name="chk_hotels_standard",
            ),
        ),
    ]
