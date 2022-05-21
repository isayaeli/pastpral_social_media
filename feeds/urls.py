from django.urls import path
from .import views
urlpatterns = [
    path('', views.feeds, name='feeds' ),
    path('delete-post/<int:id>', views.delete_feed, name='delete_feed')
]