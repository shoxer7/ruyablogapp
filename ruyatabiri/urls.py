from django.contrib import admin
from django.urls import path
from . import views
app_name = "ruyatabiri"

urlpatterns = [
    
    path('ruyatabiridetay/<int:id>',views.ruyatabiridetay, name="ruyatabiridetay"),
    path('ruyatabiri/<char>/', views.ruya_tabir_liste, name="ruya_tabir_liste" ),
] 
