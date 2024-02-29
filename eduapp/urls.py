from django.urls import path 
from . import views


urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('',views.dashboard_view,name='dashboard'),
    path('about_us/',views.about_us,name='about_us'),
    path('offerings/',views.offerings,name='offerings'),
    path('membership/',views.membership,name='membership'),


]
