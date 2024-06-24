from django.shortcuts import render

from .models import (HeaderText)

def index(request):
    texts = HeaderText.objects.all().first()
    return render(request, "base.html", {"texts":texts})
