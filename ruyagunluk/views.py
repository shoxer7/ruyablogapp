from django.shortcuts import render,redirect,get_object_or_404
from .forms import RuyaGunlukForm
from .models import RuyaGunluk
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,"index.html")

@login_required(login_url = "user:login")
def dashboard(request):
    ruyagunlukleri = RuyaGunluk.objects.filter(author = request.user)
    context = {
        "ruyagunlukleri":ruyagunlukleri
    }
    return render(request, "dashboard.html",context)

@login_required(login_url = "user:login")
def addarticle(request):
    form = RuyaGunlukForm(request.POST or None)

    if form.is_valid():
        ruyagunluk = form.save(commit=False)

        ruyagunluk.author = request.user
        ruyagunluk.save()

        messages.success(request,"Rüya Başarı ile Oluşturuldu")
        return redirect("ruyagunluk:dashboard")

    return render(request, "addarticle.html",{"form" : form})

def ruyagunlukdetay(request,id):
    #ruyagunluk = RuyaGunluk.objects.filter(id=id).first()
    ruyagunluk = get_object_or_404(RuyaGunluk,id = id) 
    return render(request, "ruyagunlukdetay.html",{"ruyagunluk":ruyagunluk})

@login_required(login_url = "user:login")
def updateRuyaGunluk(request,id):
    ruyagunluk = get_object_or_404(RuyaGunluk,id = id)
    form = RuyaGunlukForm(request.POST or None, instance=ruyagunluk)
    if form.is_valid():
        ruyagunluk = form.save(commit=False)

        ruyagunluk.author = request.user
        ruyagunluk.save()

        messages.success(request,"Rüya Başarı ile Güncellendi")
        return redirect("ruyagunluk:dashboard")

    return render(request,"update.html",{"form":form})

@login_required(login_url = "user:login")
def deleteRuyaGunluk(request,id):
    ruyagunluk = get_object_or_404(RuyaGunluk, id = id)
    ruyagunluk.delete()
    messages.success(request,"Rüya Başarıyla Silindi")
    return redirect("ruyagunluk:dashboard")