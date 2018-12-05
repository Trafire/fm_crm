from django.urls import path

from . import views

app_name = 'sales'
urlpatterns = [
    path('', views.index, name='index'),
    path('sales_overview/<str:client>/<int:week>/', views.sales_overview, name='sales_overview'),

]