from django.shortcuts import render

from main.models import Mails,Messages


def index(request):
    

    return render(request,'index.html')