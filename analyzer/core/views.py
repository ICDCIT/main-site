from django.shortcuts import render


def IndexView(request):
    return render(request, 'core/index.html')
def BbsrMarket(request):
    return render(request, 'bbsr/market.html')
