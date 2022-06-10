from django.urls import path
from .import views

urlpatterns = [

    path('', views.register, name='home'),
    path('register_user', views.register_user, name='register_user'),
    path('addDetails',views.addDetails,name='addDetails'),
    path('add_data',views.add_data,name='add_data'),
    path('admin_event_view',views.admin_event_view,name='admin_event_view'),
    path('booking_details',views.booking_details,name='booking_details'),
    path('user_show_events',views.user_show_events,name='user_show_events'),
    path('login_user', views.login_user, name="login_user"),
    path('logout_user', views.logout_user, name='logout_user'),

    path('welcomeadmin/',views.welcomeadmin,name="welcomeadmin"),
    path('admin_event_details/',views.admin_event_details,name="admin_event_details"),

    path('reject_event/<int:pk>',views.reject_event,name='reject_event'),
    path('aprove_event/<int:pk>',views.aprove_event,name='aprove_event'),




    
]