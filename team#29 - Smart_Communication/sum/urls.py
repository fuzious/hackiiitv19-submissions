
from django.urls import path,include
from . import views

urlpatterns = [
    
    
    path("",views.guide,name="guide"),

]