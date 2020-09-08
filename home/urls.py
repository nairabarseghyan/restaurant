from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/<slug>', views.slug),
    path('coffee/<slug>', views.coffee),
    path('drink/<slug>', views.drink),
    path('dessert/<slug>', views.drink),
    path('service', views.service, name='service' ),
    path('viptables', views.vip, ),
    path('tables', views.tables,),
]