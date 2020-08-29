import datetime
from reservationpage.models import Table, Reservation


def check_availability(table, start_time, end_time):
    available_list = []
    reservation_list = Reservation.objects.filter(table=table)

    for reservation in reservation_list:
        if reservation.start_time > end_time or reservation.end_time < start_time:
            available_list.append(True)
        else:
            available_list.append(False)
    return all(available_list)