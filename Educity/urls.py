
from django.contrib import admin
from django.urls import path,include
from eduapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('eduapp.urls'))


   
]
