from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /file/
    url(r'^$', views.index, name='index'),
    # url(r'^uploadFile/$',views.uploadFile, name='uploadFile'),
    url(r'^imagetotextconv/$', views.imageToTextConv, name='imageToTextConv'),
    url(r'^upload/$', views.upload_file, name='upload_file'),
    url(r'returntext/$', views.returntext, name='returntext'),
    url(r'login/$', views.login, name='login'),
    url(r'message/$', views.message, name='message'),
]