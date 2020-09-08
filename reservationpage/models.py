from django.db import models
from django.conf import settings



class Table(models.Model):
    TABLE_CATEGORIES = (
        ('I', 'INDOOR TABLE'),
        ('IV', 'INDOOR VIP TABLE'),
        ('O', 'OUTDOOR TABLE'),
        ('OV', 'OUTDOOR VIP TABLE'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=2, choices = TABLE_CATEGORIES)
    chairs = models.IntegerField()

    def __str__(self):
        return f'number #{self.number} {self.category} with {self.chairs} chairs'

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has reserved {self.table} starting from {self.start_time} to {self.end_time}'



class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    time = models.CharField(max_length=10, default="DEFAULT VALUE")
    bill = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} has reserved {self.table} for {self.time} hours. Bill is {self.bill} drams'



