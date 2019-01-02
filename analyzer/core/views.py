from django.shortcuts import render


def IndexView(request):
    return render(request, 'core/index.html')

def BbsrView(request):
    return render(request, 'core/bbsr.html')

def AgraView(request):
    return render(request, 'core/agra.html')

def BbsrMarket(request):
    return render(request, 'bbsr/market.html')

def BbsrFood(request):
    return render(request, 'bbsr/food.html')

def BbsrPlaces(request):
    return render(request, 'bbsr/places.html')

def BbsrWeather(request):
    return render(request, 'bbsr/weather.html')

def BbsrCrime(request):
    return render(request, 'agra/crime.html')



def AgraMarket(request):
    return render(request, 'agra/market.html')

def AgraFood(request):
    return render(request, 'agra/food.html')

def AgraMonument(request):
    return render(request, 'agra/monument.html')

def AgraWeather(request):
    return render(request, 'agra/weather.html')

def AgraCrime(request):
    return render(request, 'agra/crime.html')
