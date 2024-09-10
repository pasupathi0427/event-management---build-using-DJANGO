
from django.contrib import admin
from django.urls import path
from myclub import views

urlpatterns = [
    
    path('' , views.home , name ='home'),
    path('home/<int:year>/<str:month>/',views.home , name='home'),
    path('events/' , views.events , name = 'list-events'),
    path('add_events', views.add_events ,name ='Add-events'), 
    path('venues/', views.venues , name ='list-venues'),
    path('show_venue/<venue_id>' , views.show_venue , name='show-venue'),
    path('add_venue/', views.add_venue ,name ='Add-venues'), 
    path('update/<venue_id>',views.update , name = 'update'),
    path('delete/<venue_id>',views.delete , name = 'delete'),
    path('update_event/<event_id>',views.update_event , name = 'update-event'),
    path('venue_text/', views.venue_text , name ='venue-text' ),
    path('venue_CSV/', views.venue_CSV , name ='venue-csv' ),
    path('venue_PDF/', views.venue_pdf , name ='venue-pdf' ),

    
]
