from django.urls import path

from manage_system import views

app_name = 'manage_system'
urlpatterns = [
    path('show_manage/',views.show_manage,name="show_manage"),
]