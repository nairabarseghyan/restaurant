from django.urls import path
from . import views
from .views import TableList, ReservationList, TableDetailView, ReservationView


urlpatterns = [
    path('', ReservationView.as_view() , name = "ReservationView"),
    path('table_list/', TableList.as_view(), name = "TableList"),
    path('reservation_list/', ReservationList.as_view(), name = "ReservationList"),
    path('<category>/', TableDetailView.as_view() , name = "TableDetailView"),

]
