from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /file/

    url(r'^(?P<question_id>[Ww][0-9]+)$', views.kycAPI, name='kycApi'),
]