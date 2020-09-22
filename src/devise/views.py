from django.shortcuts import render, HttpResponse

# Create your views here.

def dashboard(self):
    return render(self, "devise/index.html", context={""})