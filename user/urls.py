from django.urls import path

from user import views

app_name = "user"
urlpatterns=[
    path('login/',views.login,name='login'),
    path('send_code/',views.send_code,name='send_code'),
    path('loginlogic/',views.loginlogic,name='loginlogic'),
]