from django.shortcuts import render


def book_trip(request):
    return render(request, "travels/book_trip.html")

def popular_attraction(request):
    return render(request, "travels/popular_attraction.html")


