from django.urls import path
from .import views

urlpatterns = [
     path('add_event',views.addDetails,name='addDetails'),
    path('add_data',views.add_data,name='add_data'),
    path('admin_event_view',views.admin_event_view,name='admin_event_view'),
    path('booking_details',views.booking_details,name='booking_details'),
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    
]