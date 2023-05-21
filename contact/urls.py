from django.urls import path
from contact import views

app_name='contact'

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('contacts/',views.contacts, name='contacts'),
    path('store/',views.store, name='store'),
    path('services/',views.services, name='services'),
]