from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.IndexView, name='index'),
    path('bbsr_market/', views.BbsrMarket, name='bbsrmarket')
]
