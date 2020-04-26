from django.shortcuts import render
from django.http import HttpResponse

def shop(req):
    return render(req,'index.html')


def about(req):
    return render(req,'about.html')


def contact(req):
    return render(req,'contact.html')


def productview(req):
    return render(req,'product.html')


def search(req):
    return render(req,'search.html')


def tracker(req):
    return render(req,'tracker.html')


def checkout(req):
    return render(req,'checkout.html')
