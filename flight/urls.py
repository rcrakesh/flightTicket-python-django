from django.urls import path
from .import views 





# from .views import welcome, home1
urlpatterns = [
    # path("<int:id>", views.index, name="index"),
  
       path("", views.welcome, name="welcome"),
       path("home1/", views.home1, name="home1"),
       path("booking/", views.booking, name="booking"),
       path("sflight/", views.sflight, name="sflight"),
       path("plane/<int:flight_id>/", views.plane, name="plane"),
      #  path('display_tickets/<int:ticket_id>/', views.display_tickets , name='display_tickets'),
      
      #  path('aflight/', views.aflight, name='aflight'),
    # path("create/", views.create, name="create"),
    # path("add", views.add,name="add")
    ]


    #  path("v1/", views.v1, name="view1"),