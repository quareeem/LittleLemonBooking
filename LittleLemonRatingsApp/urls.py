from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('bookings/', views.bookings, name="bookings"),
    path('reservations/', views.reservations, name="reservations"),

]
