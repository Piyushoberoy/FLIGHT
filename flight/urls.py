from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("Marshall", views.MarshallIndex, name="MarshallIndex"),
    path("accounts", views.accounts, name="accounts"),
    path("MarshallLogin", views.MarshallLogin_view, name="MarshallLogin"),
    path("flights", views.MarshallFlight, name="flights"),
    path("addFlight", views.MarshallAddFlight, name="addflight"),
    path('removeFlights/', views.MarshallRemoveFlights, name='MarshallRemoveFlights'),
    path('flight/<int:flight_id>/tickets/', views.flight_tickets_view, name='flight_tickets'),
    path('passengers', views.Passengers, name='Passengers'),
    path('addPassengers/', views.AddPassengers, name='AddPassengers'),
    path('removePassengers/', views.RemovePassengers, name='RemovePassengers'),
    
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("query/places/<str:q>", views.query, name="query"),
    path("flight", views.flight, name="flight"),
    path("review", views.review, name="review"),
    path("flight/ticket/book", views.book, name="book"),
    path("flight/ticket/payment", views.payment, name="payment"),
    path('flight/ticket/api/<str:ref>', views.ticket_data, name="ticketdata"),
    path('flight/ticket/print',views.get_ticket, name="getticket"),
    path('flight/bookings', views.bookings, name="bookings"),
    path('flight/ticket/cancel', views.cancel_ticket, name="cancelticket"),
    path('flight/ticket/resume', views.resume_booking, name="resumebooking"),
    path('contact', views.contact, name="contact"),
    path('privacy-policy', views.privacy_policy, name="privacypolicy"),
    path('terms-and-conditions', views.terms_and_conditions, name="termsandconditions"),
    path('about-us', views.about_us, name="aboutus"),
]