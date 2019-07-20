from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /file/
    url(r'send/$',views.kycAPI,name='kycApi'),
    url(r'ajaximageupload/$',views.homeNew,name='homeNew'),
    url(r'mutualimageupload/$',views.mutualimageupload,name='mutualimageupload'),
    url(r'ajaximageupload1/$',views.homeNew1,name='homeNew1'),
    url(r'ajaximageupload2/$',views.homeNew2,name='homeNew2'),
    url(r'ajaxmutualupload/$',views.mutualUpload,name='mutualUpload'),
    url(r'cheque/$', views.home, name='home'),
    url(r'mutualequity/$', views.mutualequity, name='mutualequity'),
    url(r'selectimage/$', views.selectimage, name='selectimage'),
    url(r'selectimagetest/$', views.selectimagetest, name='selectimagetest'),
    url(r'returntext/$', views.returntext, name='returntext'),
    url(r'returntextAC/$', views.returntextAC, name='returntextAC'),
    url(r'returntextCrop/$', views.returntextCrop, name='returntextCrop'),
    url(r'returnmutualcroptext/$', views.returnMutualcroptext, name='returnmutualcroptext'),
    url(r'imagetotext/$', views.imagetotext, name='imagetotext'),
    url(r'imagetotextcopy/$', views.imagetotextcopy, name='imagetotextcopy'),
    url(r'test/$', views.test, name='test'),
    url(r'display/$',views.display, name='display'),
    url(r'uccbo/$',views.uccBO, name='uccbo'),
    url(r'uccupload/$',views.uccUpload, name='uccupload'),
    url(r'downloadFile/$',views.downloadFile,name='downloadFile'),
    url(r'cktest/$',views.cktest,name='cktest'),
    url(r'selectimagetestNew/$',views.selectimagetestNew,name='selectimagetestNew'),
    url(r'selectimagetestNewAjax/$',views.selectimagetestNewAjaxCrop,name='selectimagetestNewAjaxCrop'),
    url(r'ajax/$',views.ajaxfileUpload,name='ajaxfileUpload'),
    url(r'showclient',views.showClient,name='showClientDetail'),
    url(r'showmutualclient',views.showmutualClient,name='showmutualClientDetail'),
    url(r'updateclient',views.updateClient,name='updateClient'),
]