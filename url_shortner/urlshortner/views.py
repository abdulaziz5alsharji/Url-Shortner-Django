from django.shortcuts import render, redirect
from . models import Url
from uuid import uuid4
from django.http import Http404
# Create your views here.

def index(request):
    if request.method == "POST":
        link = request.POST["url"]
        uid = str(uuid4())[:5]
        if len(link) > 0:
            url = Url(link=link, uuid=uid)
            url.save()
            return render(request, "urlshortner/index.html", context={
                "new_url": f"localhost:8000/{uid}"
            })
    return render(request, "urlshortner/index.html", context={

    })

def go(request, uid: str):
    try:
        link = Url.objects.get(uuid=uid).link
    except Url.DoesNotExist:
        raise Http404("NOT FOUND")
    if "http" in link or "https" in link:
        return redirect(link)
    else:
        return redirect(f"https://{link}")

