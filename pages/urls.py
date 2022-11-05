from urllib.parse import urlparse
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blog/", views.blog, name="blog"),
    path("about-us/", views.about_us, name="about-us"),
    path("contact-us/", views.contact_us, name="contact-us"),
    path("privacy-policy/", views.privacy_policy, name="privacy-policy"),
    path("bestnewdestinations/", views.bestnewdestinations, name="bestnewdestinations"),
    path("booktrip/", views.booktrip, name="Book & Trip"),
]