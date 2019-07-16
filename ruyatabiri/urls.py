from django.contrib import admin
from django.urls import path
from . import views
app_name = "ruyatabiri"

urlpatterns = [
    
    path('ruyatabiridetay/<int:id>',views.ruyatabiridetay, name="ruyatabiridetay"),
    path('a/', views.a, name="a" ),
    path('b/', views.b, name="b" ),
    path('c/', views.c, name="c" ),
    path('ç/', views.ç, name="ç" ),
    path('d/', views.d, name="d" ),
    path('e/', views.e, name="e" ),
    path('f/', views.f, name="f" ),
    path('g/', views.g, name="g" ),
    path('h/', views.h, name="h" ),
    path('ı/', views.ı, name="ı" ),
    path('i/', views.i, name="i" ),
    path('j/', views.j, name="j" ),
    path('k/', views.k, name="k" ),
    path('l/', views.l, name="l" ),
    path('m/', views.m, name="m" ),
    path('n/', views.n, name="n" ),
    path('o/', views.o, name="o" ),
    path('ö/', views.ö, name="ö" ),
    path('p/', views.p, name="p" ),
    path('r/', views.r, name="r" ),
    path('s/', views.s, name="s" ),
    path('ş/', views.ş, name="ş" ),
    path('t/', views.t, name="t" ),
    path('u/', views.u, name="u" ),
    path('ü/', views.ü, name="ü" ),
    path('v/', views.v, name="v" ),
    path('y/', views.y, name="y" ),
    path('z/', views.z, name="z" ),


    
 
] 
