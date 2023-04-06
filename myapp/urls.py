from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings
from . import views

urlpatterns = [
    path("search/",views.search,name="search"),
    path("",views.index, name="index"),
    
    path("home",views.index, name="home"),
    path("about/",views.about, name="about"),

    path("team/",views.team, name="team"),
    path("service/",views.service, name="service"),
    path("testimonial/",views.testimonial, name="testimonial"),
    path("blog/",views.blog, name="blog"),
    path("price/",views.price, name="price"),
    path("contact/",views.contact, name="contact"),

    path("story/", views.story, name="story"),
    path("career/", views.career, name="career"),
    
    path("detail/<slug:slug>/",views.detail, name="detail"),
    path("feature/",views.feature, name="feature"),

] #+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)