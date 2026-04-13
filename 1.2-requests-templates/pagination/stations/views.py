from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open('data-398-2018-08-30.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        stations = []
        for row in reader:
            stations.append({
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District'],
            })


    paginator = Paginator(stations, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'bus_stations': page_obj,
        'page': page_obj,
    }
    return render(request, 'stations/index.html', context)
