from django.shortcuts import render,get_object_or_404
from .models import RuyaTabiri
# Create your views here.

def index(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    return render(request,"index.html")

def ruyatabiridetay(request, id):
    template_name = "ruyatabiridetay.html"
    ruyatabiri = get_object_or_404(RuyaTabiri, id = id) 
    return render(request, template_name, {"ruyatabiri":ruyatabiri})

def ruya_tabir_liste(request, char):
    template_name = "ruya_tabir_liste.html"
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request, template_name, {"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith=char.upper()).order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, template_name, context)
