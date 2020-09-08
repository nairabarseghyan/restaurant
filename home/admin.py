from django.contrib import admin
from .models import Food
from .models import Coffee
from .models import Drink
from .models import Dessert

# Register your models here.
admin.site.register(Food)
admin.site.register(Coffee)
admin.site.register(Drink)
admin.site.register(Dessert)