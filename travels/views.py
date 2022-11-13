from django.shortcuts import render
import mysql.connector


def book_trip(request):
    return render(request, "travels/book_trip.html")

