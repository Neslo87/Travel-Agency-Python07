from django.db import models
from django.db.models import Q


class Continent(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    continent = models.ForeignKey("continent", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"


class City(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    country = models.ForeignKey("country", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"


class Airport(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    iata = models.CharField(max_length=12, null=False, blank=False, primary_key=True)
    city = models.ForeignKey("city", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    city = models.ForeignKey("city", on_delete=models.CASCADE)
    standard = models.IntegerField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(standard__gte=1) & Q(standard__lte=5),
                name="chk_hotels_standard",
            )
        ]


BB = "Bed & Breakfast"
HB = "Half Board"
FB = "Full Board"
AI = "All Inclusive"
TYPE_CHOICES = [
    (BB, BB),
    (HB, HB),
    (FB, FB),
    (AI, AI),
]


class Trip(models.Model):
    from_where = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="trips_from"
    )
    to_where = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="trips_to"
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    number_of_days = models.IntegerField()
    type = models.CharField(max_length=32, choices=TYPE_CHOICES)
    price_for_an_adult = models.IntegerField(help_text=("Euro"))
    price_for_a_child = models.IntegerField(help_text=("Euro"))
    promoted = models.BooleanField()
    number_of_places_for_adults = models.IntegerField()
    number_of_places_for_children = models.IntegerField()


# class Purchase_of_a_trip(models.Model):
#     trip =
#     participant_details =
#     ammount =
