from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def kycAPI(request,question_id):
    # data1 = ''
    # if request.method == 'GET':
    #     data1 = request.GET['id']
    #     print data1

    # return HttpResponse(data1)
    return HttpResponse("You're looking at question %s." % question_id)