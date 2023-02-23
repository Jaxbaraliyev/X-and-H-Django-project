from django.shortcuts import render
from .models import *


def asosiy(request):
    qidiruv_sozi = request.GET['qidirish']
    t_soz = Togri.objects.filter(soz=qidiruv_sozi)
    if len(t_soz) > 0:
        n_soz = Notogri.objects.filter(togri=t_soz[0])
    else:
        n_soz = Notogri.objects.filter(soz=qidiruv_sozi)
    if len(n_soz) > 0:
        t_soz = [n_soz[0].togri]
        n_soz = Notogri.objects.filter(togri=t_soz[0])
    else:
        t_soz = ["bunaqa so`z yo`q"]
    data = {
        "togrisi":t_soz[0],
        "notogrisi":n_soz
    }
    return render(request,"result.html", data)

