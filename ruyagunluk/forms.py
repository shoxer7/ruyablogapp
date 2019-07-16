from django import forms
from .models import RuyaGunluk

class RuyaGunlukForm(forms.ModelForm):
    class Meta:
        model = RuyaGunluk
        fields = ["title","content"]