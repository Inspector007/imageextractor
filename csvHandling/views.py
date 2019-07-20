from django.shortcuts import render
import time
import os
import glob
from django.http import *
from django.http import HttpResponse,HttpRequest,request
from PIL import Image
#import PythonMagick
from .forms import UploadFileForm, LoginForm
# from googleOCR import xyz
from csvHandling.googleOCR import xyz
from django.views.decorators.csrf import csrf_exempt
import PythonMagick
from pyPdf import PdfFileWriter, PdfFileReader
from PIL import Image
import glob
from .models import User
# Create your views here.

@csrf_exempt
def returntext(request):

        username = request.session['username']
        print "returntest",username," dfgd"
        appname = 'csvHandling'
        data = xyz(appname,username)
        return HttpResponse(data)



def login(request):
    # if this is a POST request we need to process the form data
    #if request.session['username'] != "":

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        userid = request.POST['userId']
        userpassword = request.POST['userPassword']
        # check whether it's valid:
        print userid,"----",userpassword
        try:
            user = User.objects.get(userId = userid)
            print user.userPassword
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                form = UploadFileForm()
                request.session['username'] = user.userId
                # return HttpResponseRedirect('/upload')
                return render(request, 'csvHandling/index.html', {'form': form,'user': user})
        except User.DoesNotExist:
            raise Http404('User Not Find')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'csvHandling/login.html', {'form': form})

def message(request):
    if request.method == 'POST':
        print request.POST
    return render(request,'csvHandling/message.html')


def index(request):
    return render(request,'csvHandling/index.html',{})

def uploadFile(request):
    return render(request,'csvHandling/uploadFile.html',)

def imageToTextConv(request):
    return render(request,'csvHandling/ImageToTextConv.html',context={'c':"hello",'p':'hello1'})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # print form
        if form.is_valid():
            # print request.FILES['file']
            #handle_uploaded_file(request.FILES['file'])
            # time.sleep(10)
            if request.session.has_key('username'):
                username = request.session['username']
                handle_uploaded_file(request.FILES['file'],username)
                return render(request, 'csvHandling/ImageToTextConv.html',{'username':username})
            else:
                return render(request, 'csvHandling/login.html')
    else:

        #print 'no file selected'
        form = UploadFileForm()
        # if request.session.has_key('username'):
        #     username = request.session['username']
        #     return render(request, 'csvHandling/index.html', {'form': form,'username':username})
        # else:
        return render(request, 'csvHandling/message.html')


"""
    inputpdf = PdfFileReader(open(f, "rb"))

    for i in xrange(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("/home/puneet/Desktop/deepak/Projects/mysite/csvHandling/static/pdf-%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)
    count = 0
    pdfList = []
    for f in glob.glob('/home/puneet/Desktop/deepak/Projects/mysite/csvHandling/static/*'):
        img = PythonMagick.Image()
        img.density("300")
        img.read(f)  # read in at 300 dpi
        img.write("/home/puneet/Desktop/deepak/Projects/mysite/csvHandling/static/image-%d.jpg" % count)
        # count += 1
        pdfList.append("/home/puneet/Desktop/deepak/Projects/mysite/csvHandling/static/image-%d.jpg" % count)
        count += 1
        ##        print len(pdfList)

        # for f in pdfList:
       # print f
    return pdfList
"""
def handle_uploaded_file(f,username):
    list1 = []
    path = ""
    for i in glob.glob('/home/puneet/Desktop/deepak/Projects/mysite/csvHandling/static/*'):
        list1.append(i.split('/')[-1])
    if username not in list1:
        os.mkdir('/home/puneet/Desktop/deepak/Projects/mysite/csvHandling/static/%s' % (username))
        path = '/home/puneet/Desktop/deepak/Projects/mysite/csvHandling/static/%s' % (username)
    else:
        print "found"
    path1 = str("/home/puneet/Desktop/deepak/Projects/mysite/csvHandling/static/" + username + "/abc.jpg")
    with open(path1, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    print "path ", type(path1), type("/home/puneet/Desktop/deepak/Projects/mysite/csvHandling/static/abc.jpg")
    img = PythonMagick.Image(path1)


    img.read(path1)  # read in at 300 dpi
    imageSize = img.size()
    print "*******",imageSize.height(),"*****",imageSize.width()
    #img1 = Image.open("/home/puneet/Desktop/deepak/Projects/mysite/csvHandling/static/abc.jpg")
    #imgnew = img1.resize((1024,768))
    #imgnew.save("/home/puneet/Desktop/deepak/Projects/mysite/csvHandling/static/abc.jpg")

    img.write(path1)
"""
    img.write("/home/puneet/Desktop/deepak/Projects/mysite/csvHandling/static/image-0.jpg")

"""






















