from django.shortcuts import render

from .models import Team


# Create your views here.
# def demo(request):
#     obj=Place.objects.all()
#     return render(request, "index.html",{'result':obj})

def demo(request):
    obj=Team.objects.all()
    return render(request, "index.html",{'member':obj})
