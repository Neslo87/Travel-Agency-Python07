from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def blog(request):
    return render(request, "pages/blog.html")


def about_us(request):
    return render(request, "pages/about-us.html")

def contact_us(request):
    return render(request, "pages/contact-us.html")

def privacy_policy(request):
    return render(request, "pages/privacy-policy.html")


def bestnewdestinations(request):
    return render(request, "pages/bestnewdestinations.html")

def booktrip(request):
    return render(request, "pages/booktrip.html")









