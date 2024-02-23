from django.urls import path
from . import views

app_name='calc'
urlpatterns=[
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('',views.upload,name='upload'),
]
