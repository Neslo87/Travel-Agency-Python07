from django.shortcuts import render
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Python@2022",
    database="world_airports",
    auth_plugin="mysql_native_password",
)


def book_trip(request):
    return render(request, "travels/book_trip.html")


def popular_attraction(request):
    return render(request, "travels/popular_attraction.html")
