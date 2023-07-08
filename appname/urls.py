from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('about/',about, name='about'),
    path('insert/',insertData, name='insertData'),
    path('update/<id>', updateData, name="updateData"),
    path('delete/<id>', deleteData, name='deleteData'),
    
    


]
