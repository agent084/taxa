from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('about-us/', views.about, name="about-us"),
    path('home/', views.home, name="home"),
    path('<int:listing_id>/listingdetails/', views.listing, name="listing"),
    path('menu/', views.menu, name="menu"),
    path('profile/', views.profile, name="profile"),
    path('becomeHost/', views.becomeHost, name="becomeHost"),
    path('<int:listing_id>/userListingProfile/', views.userListingProfile, name="userListingProfile"),
    path('filters/', views.filters, name="filters"),
    path('search/', views.search, name="search"),
    path('searchclick/', views.searchclick, name="searchclick"),
    path('filterResults/', views.filterResults, name="filterResults"),
    path('searchResults/', views.searchResults, name="searchResults")
]