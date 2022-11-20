from django.shortcuts import render

from .models import Airport


def book_trip(request):
    airports = [a for a in Airport.objects.values("iata", "name").all()]
    return render(request, "travels/book_trip.html", context={"airports": airports})
