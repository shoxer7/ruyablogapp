from django.contrib import admin
from django.urls import path
from . import views

app_name = "ruyagunluk"

urlpatterns = [
   path('dashboard/', views.dashboard, name="dashboard" ),
   path('addarticle/', views.addarticle, name="addarticle" ),
   path('delete/<int:id>',views.deleteRuyaGunluk,name="delete"),
   path('update/<int:id>',views.updateRuyaGunluk,name="update"),
   path('ruyagunlukdetay/<int:id>',views.ruyagunlukdetay, name="ruyagunlukdetay"),

] 