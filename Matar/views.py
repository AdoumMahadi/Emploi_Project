from django.shortcuts import render


def home(requets):
    return render(requets, 'base.html')
