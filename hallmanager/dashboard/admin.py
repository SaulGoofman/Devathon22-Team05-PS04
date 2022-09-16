from django.contrib import admin
from .models import AllotedHall, SeminarHall, Request, Feedback

# Register your models here.

admin.site.register(Request)
admin.site.register(SeminarHall)
admin.site.register(AllotedHall)
admin.site.register(Feedback)
