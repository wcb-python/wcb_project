from django.urls import path

from banner import views

app_name = "banner"

urlpatterns = [
    path('banner_list/',views.banner_list,name="banner_list"),
    path('banner_opera/',views.banner_opera,name="banner_opera"),
]