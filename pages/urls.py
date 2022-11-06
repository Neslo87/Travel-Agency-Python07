from urllib.parse import urlparse
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about_us/", views.about_us, name="about_us"),
    path("contact_us/", views.contact_us, name="contact_us"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
    path("bestnewdestinations/", views.bestnewdestinations, name="bestnewdestinations"),
    path("booktrip/", views.booktrip, name="Book & Trip"),
]