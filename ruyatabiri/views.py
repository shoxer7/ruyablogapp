from django.shortcuts import render,get_object_or_404
from .models import RuyaTabiri
from django.contrib.sitemaps import Sitemap
# Create your views here.

class BlogSitemap(Sitemap): 
    changefreq = "daily"
    priority = 1.0
    def items(self):
        return RuyaTabiri.objects.all()
    def lastmod(self,obj):
        return obj.created_date
    def location(self,obj):
        return "/ruyatabiri/ruyatabiridetay/"+str(obj.id)


def index(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    return render(request,"index.html")

def ruyatabiridetay(request,id):
    template_name = "ruyatabiridetay.html"
    ruyatabiri = get_object_or_404(RuyaTabiri,id = id) 
    return render(request, template_name, {"ruyatabiri":ruyatabiri})

def ruya_tabiri_liste(request, char):
    template_name = "ruya_tabirleri_liste.html"
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request, template_name, {"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith=char.upper()).order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, template_name, context)



