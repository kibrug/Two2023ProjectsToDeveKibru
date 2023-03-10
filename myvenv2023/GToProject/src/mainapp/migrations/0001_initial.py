# Generated by Django 4.1.4 on 2023-01-10 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DataClass",
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
                ("info", models.CharField(max_length=255)),
                ("santase", models.IntegerField()),
                ("hits_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Facets",
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
                ("country_name", models.CharField(max_length=255)),
                ("unit_name", models.CharField(max_length=255)),
                ("currency_name", models.CharField(max_length=255)),
                ("category_name", models.CharField(max_length=255)),
                ("type_name", models.CharField(max_length=255)),
                ("group_name", models.CharField(max_length=255)),
                ("frequency_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Info",
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
                ("hits_name", models.CharField(max_length=255)),
                ("page", models.IntegerField()),
                ("facets", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Unit",
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
                ("key", models.CharField(max_length=255)),
                ("doc_count", models.IntegerField(default=0)),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mainapp.facets"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Type",
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
                ("key", models.CharField(max_length=255)),
                ("doc_count", models.IntegerField(default=0)),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mainapp.facets"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HitsMainClass",
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
                ("value", models.IntegerField(default=0)),
                ("relation", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
                ("category", models.CharField(max_length=255)),
                ("currency", models.CharField(max_length=255)),
                ("iids", models.CharField(max_length=255)),
                ("esID", models.CharField(max_length=255)),
                ("s", models.CharField(max_length=255)),
                ("importance", models.IntegerField(default=0)),
                ("name", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=255)),
                ("group", models.CharField(max_length=255)),
                ("frequency", models.CharField(max_length=255)),
                ("unit", models.CharField(max_length=255)),
                ("pretty_name", models.CharField(max_length=255)),
                ("url", models.CharField(max_length=255)),
                (
                    "dataclas",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.dataclass",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Hits",
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
                ("value", models.IntegerField(default=0)),
                ("relation", models.CharField(max_length=255)),
                (
                    "hits",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mainapp.info"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Group",
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
                ("key", models.CharField(max_length=255)),
                ("doc_count", models.IntegerField(default=0)),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mainapp.facets"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Frequency",
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
                ("key", models.CharField(max_length=255)),
                ("doc_count", models.IntegerField(default=0)),
                (
                    "frequency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mainapp.facets"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Currency",
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
                ("key", models.CharField(max_length=255)),
                ("doc_count", models.IntegerField(default=0)),
                (
                    "currency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mainapp.facets"
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
                ("key", models.CharField(max_length=255)),
                ("doc_count", models.IntegerField(default=0)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mainapp.facets"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                ("key", models.CharField(max_length=255)),
                ("doc_count", models.IntegerField(default=0)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mainapp.facets"
                    ),
                ),
            ],
        ),
    ]
