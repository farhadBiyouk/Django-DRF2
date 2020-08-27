from django.urls import path, include
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.all_person),
    path('new_person/', views.new_person),
    path('new_user/', views.new_user),
    path('search_person/', views.search_person),
    path('retrieve_person/<int:r_id>/', views.retrieve_person),
    path('del_person/<int:d_id>/', views.del_person),
    path('up_person/<int:u_id>/', views.up_person),


]