import argparse
import csv
from collections import defaultdict
from typing import Any, Optional

from django.core.management.base import BaseCommand, CommandParser

from travels.models import Continent, Country, City, Airport


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("filename", type=argparse.FileType("r"))
        return super().add_arguments(parser)

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        rows = []
        reader = csv.DictReader(options["filename"])
        for row in reader:
            rows.append(row)

        continents_lookup = {}
        # continents = []
        for name in {row["CONTINENT"] for row in rows}:
            continent = Continent(name=name)
            continent.save()
            continents_lookup[name] = continent.pk
            # continents.append(continent)

        # Continent.objects.bulk_create(continents)
        # continents_lookup = {c.name: c.pk for c in Continent.objects.all()}

        continent_countries = defaultdict(list)
        for row in rows:
            continent_countries[row["CONTINENT"]].append(row["COUNTRY"])

        countries_lookup = {}
        for continent, countries in continent_countries.items():
            continent_id = continents_lookup[continent]
            for name in set(countries):
                country = Country(name=name, continent_id=continent_id)
                country.save()
                countries_lookup[name] = country.pk

        country_cities = defaultdict(list)
        for row in rows:
            country_cities[row["COUNTRY"]].append(row["City"])

        cities_lookup = {}
        for country, cities in country_cities.items():
            country_id = countries_lookup[country]
            for name in set(cities):
                city = City(name=name, country_id=country_id)
                city.save()
                cities_lookup[name] = city.pk

        city_airports = defaultdict(list)
        for row in rows:
            city_airports[row["City"]].append((row["Airport"], row["IATA Code"]))

        for city, airports in city_airports.items():
            city_id = cities_lookup[city]
            for name, iata in airports:
                airport = Airport(name=name, iata=iata, city_id=city_id)
                airport.save()
