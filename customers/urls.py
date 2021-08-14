from . import views
from django.urls import path
app_name = "customers"
urlpatterns = [
    path('', views.home),
    path('home/' , views.home ,  name = "home"),
    
    path('view_hist/' , views.view_hist , name = "view_hist"),
    path("view_cust/",views.view_cust, name = "view_cust" ),
    path("transfer/" , views.transfer , name = "transfer"),
]
