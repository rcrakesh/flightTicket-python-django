from django.urls import path
from .import views 

# from .views import welcome, home1
urlpatterns = [
    # path("<int:id>", views.index, name="index"),
  
      #  path("", views.welcome, name="welcome"),
       path('register/', views.register, name="register"),
       path('login/', views.login, name="login"),
       path('logout', views.logout, name="logout"),
        
      #  path("booking/", views.booking, name="booking"),
 

    # path("create/", views.create, name="create"),
    # path("add", views.add,name="add")
    ]


    #  path("v1/", views.v1, name="view1"),

