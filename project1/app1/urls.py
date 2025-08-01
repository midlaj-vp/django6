from django.urls import path
from .import views

urlpatterns = [
    path('',views.election_1,name='abc'),
    path('add/',views.add_1,name='add')
]
