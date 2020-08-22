from django.shortcuts import render

reservations = [
    {
        'customer':'username',
        'table_number':'1',
        'date_reserved': 'august 29',
        'time_reserved' : '14:00-16:00'

    },
    {
        'customer':'username1',
        'table_number':'2',
        'date_reserved': 'august 28',
        'time_reserved' : '17:00-18:00'
    }
]

def reservation(request):
    context = {
        'reservations': reservations
    }
    return render(request, 'reservation/reservation_page.html', context)
