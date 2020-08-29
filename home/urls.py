from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service', views.service, name='service' ),
    path('viptables', views.vip, ),
    path('tables', views.tables,)
]