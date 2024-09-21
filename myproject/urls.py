from django.contrib import admin
from django.urls import path
from myproject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',homepage,name='homepage'),
    path('',base,name='base'),
    path('addjob/',addjob,name='addjob'),
    path('contact/',contact,name='contact'),
    path('jobdetail/',jobdetail,name='jobdetail'),
    path('dashboard/',dashboard,name='dashboard'),
    path('delete/<int:id>',delete,name='delete'),
    path('edit/<int:id>',edit,name='edit'),
    path('update/',update,name='update'),
    path('job_table/',job_table,name='job_table'),
    path('singlejob/<int:id>',singlejob,name='singlejob'),
    path('loginpage/',loginpage,name='loginpage'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('registerpage/', registerpage,name='registerpage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
