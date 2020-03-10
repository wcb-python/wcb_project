from django.urls import path

from article import views

app_name = 'article'
urlpatterns=[
    path('upload_img/',views.upload_img,name='upload_img'),
    path('get_all_upload_images/',views.get_all_upload_images,name='get_all_upload_images'),
    path('get_all_article/',views.get_all_article,name='get_all_article'),
    path('article_opea/',views.article_opea,name='article_opea'),
    path('add_article/',views.add_article,name='add_article'),
    path('update_article/',views.update_article,name='update_article'),
]