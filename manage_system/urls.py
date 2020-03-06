from django.urls import path

from manage_system import views

app_name = 'manage_system'
urlpatterns = [
    path('show_manage/',views.show_manage,name="show_manage"),
    path('show_userlist/',views.show_userlist,name="show_userlist"),
    path('update/',views.update,name="update"),
    path('bar_list/',views.bar_list,name="bar_list"),
    path('map_data/',views.map_data,name="map_data"),
]