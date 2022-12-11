from django.shortcuts import render


# Render Homepage
def home(request):
    return render(request, "index.html")


# Render opportunities page
def opportunities(request):
    return render(request, "opportunities.html")
