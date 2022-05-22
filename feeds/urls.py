from django.urls import path
from .import views
urlpatterns = [
    path('', views.feeds, name='feeds' ),
    path('edit-post/<int:id>', views.edit_feed, name='edit_feed'),
    path('delete-post/<int:id>', views.delete_feed, name='delete_feed')
]