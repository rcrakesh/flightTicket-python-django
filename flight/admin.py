from django.contrib import admin
from .models import  BookTickets
# Register your models here.

class  BookTicketsAdmin(admin.ModelAdmin):
    list_display = ('name','phone', 'email','airport1','airport2','departing_date','returning_date',)
    list_display_links  = ('name','email',)
    search_fields = ('name', 'phone' , 'email' , )
    list_filter = ('airport1','airport2',)
# admin.site.register(booking)
admin.site.register(BookTickets , BookTicketsAdmin)
