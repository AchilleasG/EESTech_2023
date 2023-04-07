from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Habit)
admin.site.register(Journey)
admin.site.register(HabitUser)
admin.site.register(JourneyUser)
admin.site.register(JourneyHabit)