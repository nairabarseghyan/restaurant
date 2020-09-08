from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View
from .models import Table, Reservation
from .forms import AvailabilityForms
from reservationpage.reservation_functions.availability import check_availability



class TableList(ListView):
    model = Table
    template_name = 'reservation/table_list'


class ReservationList(ListView):
    model = Reservation
    template_name = 'reservation/reservation_list.html'

class TableDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForms()
        table_list = Table.objects.filter(category=category)


        if len(table_list)>0:
            table = table_list[0]
            table_category = dict(table.TABLE_CATEGORIES).get(table.category, None)
            context = {
                'table_category' : table_category
            }
            return render(request, 'reservation/reservation_page.html', context)
        else:
            return HttpResponse('category does not exist')




    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        table_list = Table.objects.filter(category=category)
        form = AvailabilityForms(request.POST)

        if form.is_valid():
            data=form.cleaned_data


        available_tables = []
        for table in table_list:
            if check_availability(table, data['start_time'], data['end_time']):
                available_tables.append(table)

        if len(available_tables) > 0:
            table = available_tables[0]
            reservation = Reservation.objects.create(
                user=request.user,
                table=table,
                start_time=data['start_time'],
                end_time=data['end_time'],
            )
            reservation.save()
            return HttpResponse(reservation)
        else:
            return HttpResponse('this tables are reserved')




class ReservationView(FormView):
    form_class = AvailabilityForms
    template_name = 'reservation/reservation_page.html'

    def form_valid(self, form):
        data = form.cleaned_data
        table_list = Table.objects.filter(category=data['table_category'])
        available_tables=[]
        for table in table_list:
            if check_availability(table, data['start_time'], data['end_time']):
                available_tables.append(table)
        if len(available_tables)>0:
            table =available_tables[0]
            reservation = Reservation.objects.create(
                user=request.user,
                table=table,
                start_time=data['start_time'],
                end_time=data['end_time'],
            )
            reservation.save()
            return HttpResponse(reservation)
        else:
            return HttpResponse('this tables are reserved')

