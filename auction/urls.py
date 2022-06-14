from django import views
from django.urls import path
from .import views
urlpatterns = [
    path('auction', views.auction, name="auction"),
    path('bid/<int:id>', views.bidding, name="bid"),
    path('add-bid', views.add_bid, name="add_bid")
]