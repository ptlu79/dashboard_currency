from django.shortcuts import render, HttpResponse, redirect

import api
# Create your views here.

def redirect_home(request):
    return redirect("home", days_range=7, currencies="USD")

def dashboard(request, days_range=30, currencies="USD"):

    days, rates = api.get_rate(currencies=currencies.split(","), days=days_range)

    page_label = {7: "Semaine", 30: "Mois", 365: "Année"}.get(days_range, "personnalisé")




    return render(request, "devise/index.html", context={"data": rates, "days_labels": days, "currencies": currencies, "page_label": page_label})