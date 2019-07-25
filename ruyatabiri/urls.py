from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap 
from .views import BlogSitemap
from django.conf.urls import url

sitemaps = { 
    "blog":BlogSitemap(),
}


app_name = "ruyatabiri"

urlpatterns = [
    path('ruyatabiridetay/<int:id>',views.ruyatabiridetay, name="ruyatabiridetay"),
    path('<char>/', views.ruya_tabiri_liste, name="ruya_tabiri_liste" ),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
] 
