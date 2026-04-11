from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open('data-398-2018-08-30.csv', 'r', encoding='utf-8') as f:
        column_index = 1
        reader = csv.reader(f)
        for row in reader:
            stations = [row]

    context = {
        'bus_stations': stations,
        'page': ...,
    }
    return render(request, 'stations/index.html', context)
