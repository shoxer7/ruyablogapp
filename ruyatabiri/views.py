from django.shortcuts import render,get_object_or_404
from .models import RuyaTabiri
# Create your views here.

def index(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    return render(request,"index.html")

def ruyatabiridetay(request,id):
    ruyatabiri = get_object_or_404(RuyaTabiri,id = id) 
    return render(request, "ruyatabiridetay.html",{"ruyatabiri":ruyatabiri})

def a(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})

    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="A").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "a.html",context)

def b(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="B").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "b.html",context)

def c(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="C").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "c.html",context)

def ç(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="Ç").order_by("title")

    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "ç.html",context)
def d(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="D").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "d.html",context)

def e(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="E").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "e.html",context)

def f(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="F").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "f.html",context)

def g(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="G").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "g.html",context)

def h(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="H").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "h.html",context)

def ı(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="I").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "ı.html",context)

def i(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="İ").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "i.html",context)

def j(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="J").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "j.html",context)

def k(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="K").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "k.html",context)

def l(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="L").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "l.html",context)

def m(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="M").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "m.html",context)

def n(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="N").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "n.html",context)

def o(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="O").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "o.html",context)

def ö(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="Ö").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "ö.html",context)

def p(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="P").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "p.html",context)

def r(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="R").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "r.html",context)

def s(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="S").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "s.html",context)

def ş(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="Ş").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "ş.html",context)

def t(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="T").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "t.html",context)

def u(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="U").order_by("title")

    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "u.html",context)
def ü(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="Ü").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "ü.html",context)

def v(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="V").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "v.html",context)

def y(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="Y").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "y.html",context)

def z(request):
    keyword = request.GET.get("keyword")
    if keyword:
        ruyatabirleri = RuyaTabiri.objects.filter(title__contains = keyword)
        return render(request,"a.html",{"ruyatabirleri":ruyatabirleri})
    ruyatabirleri = RuyaTabiri.objects.filter(title__startswith="Z").order_by("title")
    context = {
        "ruyatabirleri":ruyatabirleri
    }
    return render(request, "z.html",context)


