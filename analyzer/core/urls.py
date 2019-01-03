from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.IndexView, name='index'),
    path('bbsr/', views.BbsrView, name='bbsr'),
    path('agra/', views.AgraView, name='agra'),
    path('bbsr/market/', views.BbsrMarket, name='bbsrmarket'),
    path('bbsr/food/', views.BbsrFood, name='bbsrfood'),
    path('bbsr/places/', views.BbsrPlaces, name='bbsrplaces'),
    path('bbsr/Weather/', views.BbsrWeather, name='bbsrweather'),
    path('bbsr/Crime/', views.BbsrCrime, name='bbsrcrime'),
    path('agra/market/', views.AgraMarket, name='agramarket'),
    path('agra/food/', views.AgraFood, name='agrafood'),
    path('agra/places/', views.AgraPlaces, name='agraplaces'),
    path('agra/Weather/', views.AgraWeather, name='agraweather'),
    path('agra/Crime/', views.AgraCrime, name='agracrime')
]
