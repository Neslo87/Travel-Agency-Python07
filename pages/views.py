from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def about_us(request):
    return render(request, "pages/about_us.html")

def contact_us(request):
    return render(request, "pages/contact_us.html")

def privacy_policy(request):
    return render(request, "pages/privacy_policy.html")


def bestnewdestinations(request):
    return render(request, "pages/bestnewdestinations.html")

def booktrip(request):
    return render(request, "pages/booktrip.html")









