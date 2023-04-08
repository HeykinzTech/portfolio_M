# """main URL Configuration
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from .sitemaps import CategorySitemap,PostSitemap

from django.contrib import admin
from django.urls import path,include


sitemaps = {'Category':CategorySitemap,'Post':PostSitemap}
urlpatterns = [
    path('sitemap.xml/',sitemap,{'sitemap': sitemaps}),
    path('admin/', admin.site.urls),
    path("",include('myapp.urls')),
] +  static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
