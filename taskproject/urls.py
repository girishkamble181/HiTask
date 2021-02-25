
from django.contrib import admin
from django.urls import path
from taskapp.views import home, usignup, ulogin, ulogout, uresetpass, delete ,create,logo
from news.views import newss, back
from weather.views import weatherss, backk

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('usignup/',usignup, name='usignup'),
    path('ulogin/',ulogin, name='ulogin'),
    path('ulogout/',ulogout, name='ulogout'),
    path('uresetpass/',uresetpass, name='uresetpass'),
    path('create/',create, name='create'),
    path('<id>/delete',delete, name='delete'),
    path('newss/', newss, name='newss'),
    path('back/', back, name='back'),
    path('logo/', logo, name='logo'),
    path('weatherss/', weatherss, name='weatherss'),
    path('backk/', backk, name='backk'),
]
