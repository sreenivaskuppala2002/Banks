from django.urls import path
from . import views
urlpatterns=[
   path('',views.endpoints),
    path("banklist/",views.banklist,),
]