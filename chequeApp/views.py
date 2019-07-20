from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,request, response, HttpResponseRedirect
from chequeApp.models import Document,BoDataUpload,UccDataUpload, MutualDataUpload
from chequeApp.forms import DocumentForm,UccDataForm,BoDataForm, MutualDataForm
from django.core.urlresolvers import reverse
import PythonMagick
from PIL import Image
import glob
import os
import time
from csvHandling.googleOCR import xyz,xyzCrop,xyzAC,xyzACCrop,mutualequityData
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
import urllib2
import urllib
import csv
#from django.core.servers.basehttp import FileWrapper
from wsgiref.util import FileWrapper
import shutil
from cusRicoMCXNew import analysisData
from ClientClass import *
from testdate import mmyydd
from dbOperation import showClientDetail,updateClientDetail,showmutualClientDetail
from Setpath import setpath
from pdftoImage import splitpdfintoimages


def kycAPI(request):
    data1 = ''
    if request.method == 'GET':
        data1 = request.GET['id']
        print data1

    return HttpResponse(data1)


@csrf_exempt
def returntext(request):
        ip = get_client_ip(request)
        data1 = {}
        imgid = 0
        if request.method == 'POST':
            print 'post call'
            print request.body
            data1 = request.body
            ip = data1.split('=')[-1]
            imgid = (data1.split('=')[1]).split('&')[0]
            print ip,'---',imgid
        #client = ClientClass()
        #ip = client.returnClientid()
        print "returntext",ip
        appname = 'chequeApp'
        data = xyz(appname,ip,imgid)
        return HttpResponse(data)

@csrf_exempt
def showClient(request):
    if request.method == 'POST':
        print request.body
        data12 = {}
        data12 = request.body
        clientid = data12.split('=')[-1]
        valList = []
        valList = showClientDetail(clientid)
        if len(valList) > 0:
            return HttpResponse(json.dumps(valList))
        else:
            return HttpResponse(json.dumps('no record found'))
    else:
        return HttpResponse("error")

@csrf_exempt
def showmutualClient(request):
    if request.method == 'POST':
        print request.body
        data12 = {}
        data12 = request.body
        clientid = data12.split('=')[-1]
        valList = []
        valList = showmutualClientDetail(clientid)
        if len(valList) > 0:
            return HttpResponse(json.dumps(valList))
        else:
            return HttpResponse(json.dumps('no record found'))
    else:
        return HttpResponse("error")



@csrf_exempt
def updateClient(request):
    if request.method == 'POST':
        print request.body
        data12 = {}
        data12 = request.body
        acholder = data12.split("=")[-1]
        ifscno = (data12.split("=")[-2]).split("&")[-2]
        acno = (data12.split("=")[-3]).split("&")[-2]
        clientid = (data12.split("=")[1]).split("&")[0]
        acholder = acholder.replace('+',' ')
        flag = updateClientDetail(clientid,acno,ifscno,acholder)
        print acholder,ifscno,acno,clientid
        if flag == 1:
            return HttpResponse(json.dumps("Record Updated Successfully"))
        else:
            return HttpResponse(json.dumps("Sorry Error"))
    else:
        return HttpResponse(json.dumps("Error"))


@csrf_exempt
def returntextCrop(request):
        '''ip = get_client_ip(request)
        print "returntext",ip
        appname = 'chequeApp'
        data = xyzCrop(appname,ip)
        return HttpResponse(json.dumps(data))'''
        if request.method == 'POST':
            ip = get_client_ip(request)
            print "returntext", ip
            appname = 'chequeApp'

            data12 = {}
            print 'post call'
            print request.body
            data12 = request.body
            ip = data12.split('=')[-1]
            imgid = (data12.split('=')[1]).split('&')[-2]
            print ip,"imageid===",imgid

            data = xyzACCrop(appname, ip,imgid)

            dictData = {'ac': '', 'ifsc': ''}
            # for i in data:
            #     print i
            data1 = json.dumps(data)
            print 'data1', data1
            print data, 'in Views', type(data), "-----", type(data1)

            # if data[1] != None:
            #     print data[1].upper()
            #     data[1] = data[1].upper()
                 # response1 = urllib2.urlopen("http://banksifsccode.com/%s/"% data[1].upper()).read()
                # print response1.head()
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponse('string Not Captured')

@csrf_exempt
def returnMutualcroptext(request):
        '''ip = get_client_ip(request)
        print "returntext",ip
        appname = 'chequeApp'
        data = xyzCrop(appname,ip)
        return HttpResponse(json.dumps(data))'''
        if request.method == 'POST':
            ip = get_client_ip(request)
            print "returntext", ip
            appname = 'chequeApp'

            data12 = {}
            print 'post call'
            print request.body
            data12 = request.body
            cropvalue = data12.split('=')[-1]
            ip = data12.split('=')[-2].split('&')[0]
            imgid = (data12.split('=')[1]).split('&')[-2]
            print ip,"imageid===",imgid,"cropvalue",cropvalue

            data = mutualequityData(appname, ip,imgid,cropvalue)

            dictData = {'ac': '', 'ifsc': ''}
            # for i in data:
            #     print i
            data1 = json.dumps(data)
            print 'data1', data1
            print data, 'in Views', type(data), "-----", type(data1)

            # if data[1] != None:
            #     print data[1].upper()
            #     data[1] = data[1].upper()
                 # response1 = urllib2.urlopen("http://banksifsccode.com/%s/"% data[1].upper()).read()
                # print response1.head()
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponse('string Not Captured')

@csrf_exempt
def returntextAC(request):
    if request.method == 'POST':
        ip = get_client_ip(request)
        print "returntext",ip
        appname = 'chequeApp'
        data12 = {}
        print 'post call'
        print request.body
        data12 = request.body
        ip = data12.split('=')[-1]
        imgid = (data12.split('=')[1]).split('&')[0]
        print ip,'-------',imgid

        data = xyzAC(appname,ip)

        dictData = {'ac':'','ifsc':''}
        # for i in data:
        #     print i
        data1 = json.dumps(data)
        print 'data1', data1
        print data,'in Views',type(data),"-----",type(data1)
        # if data[1] != '':
        #     print data[1].upper()
        #     data[1] = data[1].upper()
            #response1 = urllib2.urlopen("http://banksifsccode.com/%s/"% data[1].upper()).read()
            #print response1.head()
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse('string Not Captured')

def home1(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('home'))
    else:
        form = DocumentForm()  # A empty, unbound form
    # Load documents for the list page
    documents = Document.objects.all()
    # Render list page with the documents and the form
    return render(
        request, 'chequeApp/chequeApp.html',{'documents': documents, 'form': form}
    )

def selectimage(request):
    ip = get_client_ip(request)
    widthImage = 1024
    heightImage = 768
    pathFix = setpath()
    path1 = str(pathFix+"/chequeApp/static/"+ ip + "/abc.jpg")
    img = PythonMagick.Image(path1)
    img.read(path1)  # read in at 300 dpi
    imageSize = img.size()
    print "*******crop image", imageSize.height(), "*****crop image", imageSize.width()
    crpImageHeight = imageSize.height()
    crpImageWidth = imageSize.width()
    widthRatio = int(crpImageWidth/widthImage)
    heightRatio = int(crpImageHeight/heightImage)

    if request.method == 'POST':
        x1 = request.POST['x1']
        x2 = request.POST['x2']
        y1 = request.POST['y1']
        y2 = request.POST['y2']
        mainImgPath = str(pathFix+"/chequeApp/static/" + ip + "/abc.jpg")
        img = Image.open(mainImgPath)
        imgCrop = img.crop((int(x1),int(y1),int(x2),int(y2)))
        cropImgPath = str(pathFix+"/chequeApp/static/" + ip + "/abcCrop.jpg")
        imgCrop.save(cropImgPath)
        print x1,x2,y1,y2
        return render(request,'chequeApp/selectPixel.html',{'x1':x1,'y1':y1,'x2':x2,'y2':y2})
    else:
        return render(request, 'chequeApp/selectPixel.html')

def selectimagetest(request):
    ip = get_client_ip(request)
    widthImage = 1024.0
    heightImage = 768.0
    pathFix = setpath()
    path1 = str(pathFix+"/chequeApp/static/" + ip + "/abc.jpg")
    img = PythonMagick.Image(path1)
    img.read(path1)  # read in at 300 dpi
    imageSize = img.size()
    print "*******crop image", imageSize.height(), "*****crop image", imageSize.width()
    crpImageHeight = imageSize.height()*1.0
    crpImageWidth = imageSize.width()*1.0
    widthRatio = crpImageWidth / widthImage
    heightRatio = crpImageHeight / heightImage
    print widthRatio,'*****',heightRatio

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        x1 = float(request.POST['x1'])
        x2 = float(request.POST['x2'])
        y1 = float(request.POST['y1'])
        y2 = float(request.POST['y2'])
        mainImgPath = str(pathFix+"/chequeApp/static/" + ip + "/abc.jpg")
        img = Image.open(mainImgPath)
        print x1, y1, x2, y2
        imgCrop = img.crop((int(x1*widthRatio), int(y1*heightRatio), int(x2*widthRatio), int(y2*heightRatio)))
        cropImgPath = str(pathFix+"/chequeApp/static/" + ip + "/abcCrop.jpg")
        imgCrop.save(cropImgPath)
        return render(request, 'chequeApp/imagetotextcopy.html',
                      {'form': form, 'ip': ip, 'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})
    else:
        form = DocumentForm()
        return render(request, 'chequeApp/imagetotextcopy.html', {'form': form, 'ip': ip})
        #return render(request, 'chequeApp/selectPixel.html')


def selectimagetestNew(request):
    ip = get_client_ip(request)
    data12 = {}
    pathFix = setpath()
    if request.method == 'POST':
        print 'post call'
        print request.body
        data12 = request.body
        ip = (data12.split('=')[-2]).split('&')[-2]
        print ip
    widthImage = 1024.0
    heightImage = 768.0
    path1 = str(pathFix+"/chequeApp/static/" + ip + "/abc.jpg")
    img = PythonMagick.Image(path1)
    img.read(path1)  # read in at 300 dpi
    imageSize = img.size()
    print "*******crop image", imageSize.height(), "*****crop image", imageSize.width()
    crpImageHeight = imageSize.height()*1.0
    crpImageWidth = imageSize.width()*1.0
    widthRatio = crpImageWidth / widthImage
    heightRatio = crpImageHeight / heightImage
    print widthRatio,'*****',heightRatio

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        x1 = float(request.POST['x1'])
        x2 = float(request.POST['x2'])
        y1 = float(request.POST['y1'])
        y2 = float(request.POST['y2'])
        mainImgPath = str(pathFix+"/chequeApp/static/" + ip + "/abc.jpg")
        img = Image.open(mainImgPath)
        print x1, y1, x2, y2
        imgCrop = img.crop((int(x1*widthRatio), int(y1*heightRatio), int(x2*widthRatio), int(y2*heightRatio)))
        cropImgPath = str(pathFix+"/chequeApp/static/" + ip + "/abcCrop.jpg")
        imgCrop.save(cropImgPath)
        return render(request, 'chequeApp/chequeApp.html',
                      {'form': form, 'ip': ip, 'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})
    else:
        form = DocumentForm()
        return render(request, 'chequeApp/chequeApp.html', {'form': form, 'ip': ip})
        #return render(request, 'chequeApp/selectPixel.html')
        #return render(request, 'chequeApp/chequeApp.html', {'form': form, 'ip': ip})


@csrf_exempt
def selectimagetestNewAjaxCrop(request):
    import pdb;pdb.set_trace()
    ip = get_client_ip(request)
    data12 = {}
    imgid = 0
    pathFix = setpath()
    if request.method == 'POST':
        print 'post call'
        print request.body
        data12 = request.body
        ip = (data12.split('=')[2]).split('&')[-2]
        imgid = (data12.split('=')[1]).split('&')[-2]
        print ip,'-------',imgid
    widthImage = 1024.0
    heightImage = 768.0
    path1 = str(pathFix+"/chequeApp/static/" + ip + "/abc%s.jpg" %(imgid))
    img = PythonMagick.Image(path1)
    img.read(path1)  # read in at 300 dpi
    imageSize = img.size()
    print "*******crop image", imageSize.height(), "*****crop image", imageSize.width()
    crpImageHeight = imageSize.height()*1.0
    crpImageWidth = imageSize.width()*1.0
    widthRatio = crpImageWidth / widthImage
    heightRatio = crpImageHeight / heightImage
    print widthRatio,'*****',heightRatio

    if request.method == 'POST':
        #form = DocumentForm(request.POST, request.FILES)
        x1 = float((data12.split('=')[3]).split('&')[-2])#(request.POST['x1'])
        x2 = float((data12.split('=')[5]).split('&')[-2])#(request.POST['x2'])
        y1 = float((data12.split('=')[4]).split('&')[-2])#(request.POST['y1'])
        y2 = float((data12.split('=')[-1]))#(request.POST['y2'])
        mainImgPath = str(pathFix+"/chequeApp/static/" + ip + "/abc%s.jpg" %(imgid))
        img = Image.open(mainImgPath)
        print x1, y1, x2, y2
        imgCrop = img.crop((int(x1*widthRatio), int(y1*heightRatio), int(x2*widthRatio), int(y2*heightRatio)))
        cropImgPath = str(pathFix+"/chequeApp/static/" + ip + "/abcCrop%s.jpg" %(imgid))
        imgCrop.save(cropImgPath)
        #return render(request, 'chequeApp/chequeApp.html',
         #             {'form': form, 'ip': ip, 'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})
        print 'if Ajax Crop ', ip
        return HttpResponse(ip)
    else:
        form = DocumentForm()
        #return render(request, 'chequeApp/chequeApp.html', {'form': form, 'ip': ip})
        #data = xyzCrop(appname, ip)
        data ="Error"
        print 'else',ip
        return HttpResponse(ip)
        #return render(request, 'chequeApp/selectPixel.html')
        #return render(request, 'chequeApp/chequeApp.html', {'form': form, 'ip': ip})

def home(request):
    # ip = get_client_ip(request)
    # if request.COOKIES['username']
    # print x
    ip = ""
    if 'username' in request.COOKIES:
        ip = request.COOKIES['username']
    else:
        print "no"
        ip = ""
    print ip,"----------------------------------------"
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            t = handle_uploaded_file(request.FILES['docfile'],ip)
            return render(request, 'chequeApp/chequeApp.html', {'form': form, 'ip':ip})
    else:
        form = DocumentForm()
    return render(request, 'chequeApp/chequeApp.html', {'form': form, 'ip':ip})


def mutualequity(request):
    return render(request, 'chequeApp/mutualequity.html')
    #return render(request, 'chequeApp/mutualequity.html')

@csrf_exempt
def mutualimageupload(request):
    # ip = get_client_ip(request)
    # if request.COOKIES['username']
    # print x
    # ip = get_client_ip(request)
    data1 = {}
    imgid = 0
    pathfix = setpath()
    if request.method == 'POST':
        print 'post call'
        print request.body
        data1 = request.body
        imgid = data1.split('=')[-1]
        ip = (data1.split('=')[1]).split('&')[0]
        print ip, '---', imgid
        path1 = pathfix+"/chequeApp/static/"+ip+"/imgFile/page_-"+imgid+".jpg"
        t = handle_uploaded_fileX(path1,ip)
        return HttpResponse(t)
    else:
        return HttpResponse("error happen")
    # return HttpResponse("Error")

def homeNew(request):
    # ip = get_client_ip(request)
    # if request.COOKIES['username']
    # print x
    ip = ""
    print 'homenew called'
    if 'username' in request.COOKIES:
        ip = request.COOKIES['username']
    else:
        print "no"
        ip = ""

    print ip,"----------------------------------------"
    if request.method == 'POST':
        ip = request.POST['loginId']
        print "in post --- ",ip
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # t = handle_uploaded_fileX("/home/puneet/Desktop/deepak/Projects/MysiteV1/mysitev1.1/mysite/chequeApp/static/E67386/imgFile/page_-1.jpg",ip)
            # f = file("/home/puneet/Desktop/deepak/Projects/MysiteV1/mysitev1.1/mysite/chequeApp/static/E67386/imgFile/page_-0.jpg")
            t = handle_uploaded_file(request.FILES['docfile'],ip)
            return HttpResponse(t)
    else:
        return HttpResponse(ip)
    return HttpResponse(ip)


def homeNew1(request):
    # ip = get_client_ip(request)
    # if request.COOKIES['username']
    # print x
    ip = ""
    print 'homenew1 called'
    if 'username' in request.COOKIES:
        ip = request.COOKIES['username']
    else:
        print "no1"
        ip = ""

    print ip,"----------------------------------------"
    if request.method == 'POST':
        ip = request.POST['loginId']
        print "in post1 --- ",ip
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            t = handle_uploaded_file1(request.FILES['docfile'],ip)
            return HttpResponse(t)
    else:
        return HttpResponse(ip)
    return HttpResponse(ip)

def homeNew2(request):
    # ip = get_client_ip(request)
    # if request.COOKIES['username']
    # print x
    ip = ""
    print 'homenew2 called'
    if 'username' in request.COOKIES:
        ip = request.COOKIES['username']
    else:
        print "no2"
        ip = ""
    print ip,"----------------------------------------"
    if request.method == 'POST':
        ip = request.POST['loginId']
        print "in post2 --- ",ip
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            t = handle_uploaded_file2(request.FILES['docfile'],ip)
            return HttpResponse(t)
    else:
        return HttpResponse(ip)
    return HttpResponse(ip)


@csrf_exempt
def imagetotext(request):
    ip = ""
    if 'username' in request.COOKIES:
        ip = request.COOKIES['username']
    else:
        print "no"
        ip = ""
    print ip, "----------------------------------------"
    if request.method == 'POST':
        ip = request.POST['loginId']
        #loginId = ClientClass(ip)
        print ip,'in Image to text'
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['docfile'],ip)
            return render(request, 'chequeApp/imagetotext.html', {'form': form, 'ip':ip})
    else:
        form = DocumentForm()
    return render(request, 'chequeApp/imagetotext.html', {'form': form, 'ip':ip})

@csrf_exempt
def imagetotextcopy(request):
    ip = get_client_ip(request)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['docfile'], ip)
            return render(request, 'chequeApp/imagetotextcopy.html', {'form': form, 'ip': ip})
    else:
        form = DocumentForm()
    return render(request, 'chequeApp/imagetotextcopy.html', {'form': form, 'ip': ip})

def handle_uploaded_fileX(f,ip):
    list1 = []
    print ' handle_uploaded_fileX',ip
    path = ""
    pathFix = setpath()
    for i in glob.glob(pathFix+'/chequeApp/static/*'):
        list1.append(i.split('/')[-1])
    if ip not in list1:
        os.mkdir(pathFix+'/chequeApp/static/%s' % (ip))
        path = pathFix+'/chequeApp/static/%s' % (ip)
    else:
        print "found"
    path1 = str(f)
    # with open(path1, 'wb+') as destination:
    #     for chunk in f.chunks():
    #         destination.write(chunk)
    #
    # print "path ", type(path1), type(path1),path1
    img1 = PythonMagick.Image()
    imgDisplay = PythonMagick.Image()
    img1.density("300")
    imgDisplay.density("300")
    img1.read(path1)  # read in at 300 dpi
    imgDisplay.read(path1)
    path1 = str(pathFix + "/chequeApp/static/" + ip + "/abc.jpg")
    str1 = str(time.time()).replace('.','')
    pathDisplay = str(pathFix + "/chequeApp/static/" + ip + "/abc%s.jpg" %(str1))
    print type(path1), "----", type(pathDisplay),"*******", type(str1)
    img1.write(path1)
    imgDisplay.write(pathDisplay)
    img = PythonMagick.Image(path1)
    img.read(path1)  # read in at 300 dpi
    imageSize = img.size()
    print "*******", imageSize.height(), "*****", imageSize.width()
    #img1 = Image.open(path1)
    #imgnew = img1.resize((854,1260))
    #imgnew.save(path1)
    img.write(path1)
    return "abc%s.jpg" %(str1)



def handle_uploaded_file(f,ip):
    list1 = []
    print ' handle_uploaded_file',ip
    path = ""
    pathFix = setpath()
    for i in glob.glob(pathFix+'/chequeApp/static/*'):
        list1.append(i.split('/')[-1])
    if ip not in list1:
        os.mkdir(pathFix+'/chequeApp/static/%s' % (ip))
        path = pathFix+'/chequeApp/static/%s' % (ip)
    else:
        print "found"
    path1 = str(pathFix+"/chequeApp/static/" + ip + "/abc.pdf")
    with open(path1, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    print "path ", type(path1), type(path1),path1
    img1 = PythonMagick.Image()
    imgDisplay = PythonMagick.Image()
    img1.density("300")
    imgDisplay.density("300")
    img1.read(path1)  # read in at 300 dpi
    imgDisplay.read(path1)
    path1 = str(pathFix+"/chequeApp/static/" + ip + "/abc.jpg")
    str1 = str(time.time()).replace('.','')
    pathDisplay = str(pathFix + "/chequeApp/static/" + ip + "/abc%s.jpg" %(str1))
    print type(path1), "----", type(pathDisplay),"*******", type(str1)
    img1.write(path1)
    imgDisplay.write(pathDisplay)
    img = PythonMagick.Image(path1)

    img.read(path1)  # read in at 300 dpi
    imageSize = img.size()
    print "*******", imageSize.height(), "*****", imageSize.width()
    #img1 = Image.open(path1)
    #imgnew = img1.resize((854,1260))
    #imgnew.save(path1)
    img.write(path1)
    return "abc%s.jpg" %(str1)


def handle_uploaded_file1(f,ip):
    list1 = []
    print ' handle_uploaded_file1',ip
    path = ""
    pathFix = setpath()
    for i in glob.glob(pathFix+'/chequeApp/static/*'):
        list1.append(i.split('/')[-1])
    if ip not in list1:
        os.mkdir(pathFix+'/chequeApp/static/%s' % (ip))
        path = pathFix+'/chequeApp/static/%s' % (ip)
    else:
        print "found"
    path1 = str(pathFix+"/chequeApp/static/" + ip + "/abc1.pdf")
    with open(path1, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    print "path ", type(path1), type(path1),path1
    img1 = PythonMagick.Image()
    imgDisplay = PythonMagick.Image()
    img1.density("300")
    imgDisplay.density("300")
    img1.read(path1)  # read in at 300 dpi
    imgDisplay.read(path1)
    path1 = str(pathFix+"/chequeApp/static/" + ip + "/abc1.jpg")
    str1 = str(time.time()).replace('.','')
    pathDisplay = str(pathFix + "/chequeApp/static/" + ip + "/abc%s.jpg" %(str1))
    print type(path1), "----", type(pathDisplay),"*******", type(str1)
    img1.write(path1)
    imgDisplay.write(pathDisplay)
    img = PythonMagick.Image(path1)

    img.read(path1)  # read in at 300 dpi
    imageSize = img.size()
    print "*******", imageSize.height(), "*****", imageSize.width()
    #img1 = Image.open(path1)
    #imgnew = img1.resize((854,1260))
    #imgnew.save(path1)
    img.write(path1)
    return "abc%s.jpg" %(str1)


def handle_uploaded_file2(f,ip):
    list1 = []
    print ' handle_uploaded_file2',ip
    path = ""
    pathFix = setpath()
    for i in glob.glob(pathFix+'/chequeApp/static/*'):
        list1.append(i.split('/')[-1])
    if ip not in list1:
        os.mkdir(pathFix+'/chequeApp/static/%s' % (ip))
        path = pathFix+'/chequeApp/static/%s' % (ip)
    else:
        print "found"
    path1 = str(pathFix+"/chequeApp/static/" + ip + "/abc2.pdf")
    with open(path1, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    print "path ", type(path1), type(path1),path1
    img1 = PythonMagick.Image()
    imgDisplay = PythonMagick.Image()
    img1.density("300")
    imgDisplay.density("300")
    img1.read(path1)  # read in at 300 dpi
    imgDisplay.read(path1)
    path1 = str(pathFix+"/chequeApp/static/" + ip + "/abc2.jpg")
    str1 = str(time.time()).replace('.','')
    pathDisplay = str(pathFix + "/chequeApp/static/" + ip + "/abc%s.jpg" %(str1))
    print type(path1), "----", type(pathDisplay),"*******", type(str1)
    img1.write(path1)
    imgDisplay.write(pathDisplay)
    img = PythonMagick.Image(path1)

    img.read(path1)  # read in at 300 dpi
    imageSize = img.size()
    print "*******", imageSize.height(), "*****", imageSize.width()
    #img1 = Image.open(path1)
    #imgnew = img1.resize((854,1260))
    #imgnew.save(path1)
    img.write(path1)
    return "abc%s.jpg" %(str1)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        #print ip
    else:
        ip = request.META.get('REMOTE_ADDR')
        #print ip
    return ip


def display(request):
    return render(request,'chequeApp/test.html')

def cktest(request):
    return render(request,'chequeApp/cookiesTest.html')

@csrf_exempt
def test(request):
    if request.method == 'POST':
        print request.body
        data = request.body
        return HttpResponse(json.dumps(data))

def uccBO(request):
    ip = get_client_ip(request)
    form = UccDataForm()
    form1 = BoDataForm()
    msgucc = ''
    msgbo = ''
    if request.method == 'POST':
        form = UccDataForm(request.POST, request.FILES)
        form1 = BoDataForm(request.POST,request.FILES)
        return render(request, 'chequeApp/imagetotext.html', {'form': form, 'ip': ip,'form1':form1})
    else:
        form = UccDataForm()
        form1 = BoDataForm()
        return render(request,'chequeApp/uccBO.html',{'form': form, 'ip': ip,'form1':form1})

def uccUpload(request):
    # Handle file upload
    form = UccDataForm()
    form1 = BoDataForm()
    pathFix = setpath()
    lstdate = mmyydd()
    if os.path.isdir(pathFix+'/document/ucc') and os.path.isdir(pathFix+'/document/BO'):
        for i in glob.glob(pathFix+'/document/ucc/%s/%s/%s/*' % (
        lstdate[1], lstdate[0], lstdate[2])):
            os.remove(i)
        for i in glob.glob(pathFix+'/document/bo/%s/%s/%s/*' % (
        lstdate[1], lstdate[0], lstdate[2])):
            os.remove(i)
    #shutil.rmtree('/home/puneet/Desktop/deepak/Projects/mysite/document/bo/')
    #shutil.rmtree('/home/puneet/Desktop/deepak/Projects/mysite/document/ucc/')
    if request.method == 'POST':
        form = UccDataForm(request.POST, request.FILES)
        form1 = BoDataForm(request.POST, request.FILES)
        if form.is_valid():
            instance = UccDataUpload(uccfile=request.FILES['uccfile'])
            instance.save()
            newdoc1 = BoDataUpload(bofile=request.FILES['bofile'])
            newdoc1.save()
            # Redirect to the document list after POST

            return render(request, 'chequeApp/uccBO.html', {'form': form, 'form1': form1, 'msgucc':'SUCCESSFULLY STORED'})
            #return HttpResponseRedirect(reverse('chequeApp.views.uccBo'),{'msgucc':'successfully stored'})
    else:
          return render(request, 'chequeApp/uccBO.html',{'form':form,'form1':form1, 'msgucc':'ERROR DURING UPLOAD'})

def mutualUpload(request):
    # Handle file upload
    form = MutualDataForm()
    pathFix = setpath()
    print "mutual entry",time.ctime()
    if os.path.isdir(pathFix+'/document/mutualequity'):
        for i in glob.glob(pathFix+'/document/mutualequity/*'):
            os.remove(i)
    #shutil.rmtree('/home/puneet/Desktop/deepak/Projects/mysite/document/bo/')
    #shutil.rmtree('/home/puneet/Desktop/deepak/Projects/mysite/document/ucc/')
    if request.method == 'POST':
        cid = request.POST['cid']
        pwd = request.POST['pwd']

        print "in post --- ", cid,"pwd", pwd
        form = MutualDataForm(request.POST, request.FILES)
        if form.is_valid():
            instance = MutualDataUpload(mutualfile=request.FILES['mutualfile'])
            instance.save()
            address = ""
            if os.path.isdir(pathFix + '/document/mutualequity'):
                for i in glob.glob(pathFix + '/document/mutualequity/*'):
                    address = i
                    print address

            if os.path.isdir('%s/chequeApp/static/%s' % (pathFix,cid)) == True:
                os.system("pdftk %s input_pw %s output %s/chequeApp/static/%s/crack.pdf" %(address,pwd,pathFix,cid))
            else:
                os.mkdir('%s/chequeApp/static/%s' % (pathFix,cid))
                os.system("pdftk %s input_pw %s output %s/chequeApp/static/%s/crack.pdf" % (address, pwd, pathFix, cid))

            #split PDF and convert it into image
            imglist = splitpdfintoimages(cid,'%s/chequeApp/static/%s' % (pathFix,cid))

            if os.path.isdir('%s/chequeApp/static/%s/output' % (pathFix, cid)) == False:
                os.mkdir('%s/chequeApp/static/%s/output' % (pathFix, cid))
            shutil.make_archive(pathFix + '/chequeApp/static/imgFile', 'zip', pathFix + '/chequeApp/static/'+cid+'/imgFile/')
            """filename = pathFix + '/mysite/chequeApp/static/imgFile.zip'
            wrapper = FileWrapper(file(filename))
            response = HttpResponse(wrapper, content_type='application/x-zip-compressed')
            response['Content-Length'] = os.path.getsize(filename)
            response['Content-Disposition'] = 'attachment; filename="result.zip"'"""
            print "mutual Exit", time.ctime()
            return HttpResponse("SUCCESSFULLY STORED+"+cid+"+"+str(imglist))
    else:
        HttpResponse("Error during Upload")
    HttpResponse("Error during Upload")



@csrf_exempt
def downloadFile(request):
    analysisData()
    pathFix = setpath()
    shutil.make_archive(pathFix+'/mysite/document/result', 'zip', pathFix+'/mysite/document/output/')
    filename = pathFix+'/mysite/document/result.zip'
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='application/x-zip-compressed')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename="result.zip"'
    # shutil.rmtree('/home/puneet/Desktop/deepak/Projects/mysite/document/bo/')
    # shutil.rmtree('/home/puneet/Desktop/deepak/Projects/mysite/document/ucc/')
    return response


def ajaxfileUpload(request):
    return render(request,"chequeApp/ajaxFileUpload.html")


def filuploaddata(request):
    if request.method == 'POST':
        print request.body
    return HttpResponse("hello")


