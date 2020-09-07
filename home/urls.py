from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/<slug>', views.slug, name='slug'),
    path('service', views.service, name='service' ),
    path('viptables', views.vip, ),
    path('tables', views.tables,),
]