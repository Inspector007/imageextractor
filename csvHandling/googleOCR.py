import argparse
# [START detect_text]
import base64
import os
import re
import sys
from googleapiclient import discovery
from googleapiclient import errors
import nltk
from nltk.stem.snowball import EnglishStemmer
from oauth2client.client import GoogleCredentials
# import redis
from bs4 import BeautifulSoup
# import textindex
from PIL import Image
import difflib
import PythonMagick
from chequeApp.Setpath import setpath
from geotext import GeoText
from chequeApp.tes import stateResult
import json
# index = textindex.Index()
# export GOOGLE_APPLICATION_CREDENTIALS=/home/administrator/Documents/AngelFiles/payInOutAutomation/pycode/imageRec-7dc836c3973a.json
# export GOOGLE_APPLICATION_CREDENTIALS=/var/projects/dev/deepak/imagetotextconversionV4/csvHandling/imageRec-7dc836c3973a.json
# export GOOGLE_APPLICATION_CREDENTIALS=/home/puneet/Desktop/deepak/ProjectsV1v1.1/csvHandling/imageRec-7dc836c3973a.json
DISCOVERY_URL = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'  # noqa
BATCH_SIZE = 10

class VisionApi:
    """Construct and use the Google Vision API service."""
    # def __init__(self, api_discovery_file='/home/administrator/Documents/AngelFiles/payInOutAutomation/pycode/imageRec-7dc836c3973a.json'):
    def __init__(self,
                 api_discovery_file='%s/csvHandling/visioncredential.json' %(setpath())):
    #visioncredential
        self.credentials = GoogleCredentials.get_application_default()
        self.service = discovery.build(
            'vision', 'v1', credentials=self.credentials,
            discoveryServiceUrl=DISCOVERY_URL)

    def detect_text(self, filename, num_retries=3, max_results=6):
        """Uses the Vision API to detect text in the given file.
        """
        images = {}

        with open(filename, 'rb') as image_file:
            images[filename] = image_file.read()

        batch_request = []
        for filename in images:
            batch_request.append({
                'image': {
                    'content': base64.b64encode(
                        images[filename]).decode('UTF-8')
                },
                'features': [{
                    'type': 'TEXT_DETECTION',
                    'maxResults': max_results,
                }]
            })
        request = self.service.images().annotate(
            body={'requests': batch_request})

        try:
            responses = request.execute(num_retries=num_retries)
            if 'responses' not in responses:
                return {}
            text_response = {}
            for filename, response in zip(images, responses['responses']):
                if 'error' in response:
                    print("API Error for %s: %s" % (
                        filename,
                        response['error']['message']
                        if 'message' in response['error']
                        else ''))
                    continue
                if 'textAnnotations' in response:
                    text_response[filename] = response['textAnnotations']
                else:
                    text_response[filename] = []
            return text_response
        except errors.HttpError as e:
            print("Http Error for %s: %s" % (filename, e))
        except KeyError as e2:
            print("Key error: %s" % e2)


def extract_description(texts):

    """Returns all the text in text annotations as a single string"""
    document = ''
    for text in texts:
        try:
            document += text['description']
        except KeyError as e:
            print('KeyError: %s\n%s' % (e, text))
            #    document =  (document).replace('\n',' ')
    print("extract_description",document)



def extract_descriptions(input_filename, texts):
    """Gets and indexes the text that was detected in the image."""
    if texts:
        document = extract_description(texts)
        # index.add(input_filename, document)
        # sys.stdout.write('.')  # Output a progress indicator.
        sys.stdout.flush()
    else:
        if texts == []:
            print('%s had no discernible text.' % input_filename)
            # index.set_contains_no_text(input_filename)


# if __name__ == '__main__':

def xyz(appname,username,imgid):
    print "username ",username
    print "appname", appname
    print "imgid", imgid
    pathFix = setpath()
    f = '%s/%s/static/%s/abc%s.jpg'%(pathFix,appname,username,imgid)
    vision = VisionApi()
    #	image_file = Image.open(f) # open colour image
    #        image_file = image_file.convert('1') # convert image to black and white
    #        image_file.save(f)

    print("vision api has been instantiated..passsing image file next step..")
    texts = vision.detect_text(f)
    # ("/home/administrator/Documents/AngelFiles/imageTxtExt/images/hem/SCAN_COPY_0002.jpg")
    #	print re.findall(r"Bill Amount After Due Date+.+Due Date applicable for current bill amount only",str(texts))

    # "/home/axdministrator/Documents/AngelFiles/imageTxtExt/images/DKYC/jpg/prefix-7.png") #/home/administrator/Documents/AngelFiles/imageTxtExt/images/ekyc/prefix-07.png")
    imagetext = []
    extText = []
    try:
        for filename, text in texts.items():
            k = extract_descriptions(filename, text)
            extText.append(k)
            print("extText : ",extText)
            imagetext.append(text[0][u'description'])
            # print(text)
            # print(text)
            # print texts
            # print(texts)
            # soup = BeautifulSoup(texts)
            # print soup
            #	 f=open("/home/administrator/Documents/AngelFiles/payInOutAutomation/dumpofimagetext.txt",'w')
            #	 f.write(texts)
        k = ' '.join(imagetext)
        idx = k.find(str(400069))#360006,400069
        # print idx

        # subs = s[:idx+1]
        # print subs
        k = k[idx - 120:idx + 6]
        imagetext1 = []
        print (imagetext[0].split('\n'))[2],(imagetext[0].split('\n'))[3]
        print(imagetext[0].split('\n'))
        imagetext1 = []
        for i in imagetext[0].split('\n'):
            imagetext1.append(i.lower())
        nameMatch = difflib.get_close_matches('RATANBEN VALJIBHAI BALASARA'.lower(),imagetext1)
        # pattern = 0.0
        # count = 0
        # if len(nameMatch) == 0:
        #     for ij in imagetext1:
        #         pattern = difflib.SequenceMatcher(None,'RATANBEN VALJIBHAI BALASARA'.lower(),ij).ratio()
        #         print pattern
        #         count += 1
        #         if count == 5:
        #             break
        print(nameMatch)
        print(imagetext1)
        accountno = []
        acifsc = []
        '''for i in imagetext1:
            print i
            p = re.findall(r'[0-9]{8,20}',i.replace(' ',''))
            print 'p',p
            if len(p) > 0:
                accountno.append(p)

            q = re.findall(r'[a-z]{2,4}[0-9]{7,11}', i.replace(' ',''))
            print 'q',q
            if len(q) > 0:
                acifsc.append(q)
        print "---",accountno[0]
        print "---",acifsc[0]'''

        print("k : ",k)
        return imagetext
    except:
        pass

# xyz()
def xyzAC(appname,username):
    print "username ",username
    print "appname", appname
    pathFix = setpath()
    f = '%s/%s/static/%s/abc.jpg'%(pathFix,appname,username)
    vision = VisionApi()
    #	image_file = Image.open(f) # open colour image
    #        image_file = image_file.convert('1') # convert image to black and white
    #        image_file.save(f)

    print("vision api has been instantiated..passsing image file next step..")
    texts = vision.detect_text(f)
    # ("/home/administrator/Documents/AngelFiles/imageTxtExt/images/hem/SCAN_COPY_0002.jpg")
    #	print re.findall(r"Bill Amount After Due Date+.+Due Date applicable for current bill amount only",str(texts))

    # "/home/axdministrator/Documents/AngelFiles/imageTxtExt/images/DKYC/jpg/prefix-7.png") #/home/administrator/Documents/AngelFiles/imageTxtExt/images/ekyc/prefix-07.png")
    imagetext = []
    extText = []
    try:
        for filename, text in texts.items():
            k = extract_descriptions(filename, text)
            extText.append(k)
            print("extText : ",extText)
            imagetext.append(text[0][u'description'])
            # print(text)
            # print(text)
            # print texts
            # print(texts)
            # soup = BeautifulSoup(texts)
            # print soup
            #	 f=open("/home/administrator/Documents/AngelFiles/payInOutAutomation/dumpofimagetext.txt",'w')
            #	 f.write(texts)
        k = ' '.join(imagetext)
        #idx = k.find(str(400069))#360006,400069
        # print idx
        print k
        # subs = s[:idx+1]
        # print subs
        #k = k[idx - 120:idx + 6]
        imagetext1 = []
        for i in imagetext[0].split('\n'):
            imagetext1.append(i)

        print(imagetext1)
        accountno = []
        acifsc = []
        for i in imagetext1:
            print i
            flag = 0
            p = re.findall(r'[0-9]{8,20}',i.replace(' ',''))
            print 'p', p
            if len(p) > 0:
                accountno.append(p)
                flag = 1
            if flag == 0:
                q = re.findall(r'[a-zA-Z]{2,4}[0-9]{7,8}', i.replace(' ',''))
                print 'q',q
                if len(q) > 0:
                    acifsc.append(q)
            else:
                continue
        #print "---A/c NO",accountno[0]
        #print "---Ifsc Code",acifsc[0]
        data = []
        if len(accountno) > 0:
            data.append(''.join(accountno[0]))
            print "---A/c NO", accountno[0]
        else:
            print 'not Found Ac no'
            data.append('Not Found')

        if len(acifsc) > 0:
            data.append(''.join(acifsc[0]))
            print "---Ifsc Code", acifsc[0]
        else:
            data.append('Not Found IFSc code')
        #print("k : ",k)
        #data = accountno[0]
        data.append(imagetext)
        print 'data',data
        return data
    except:
        pass

def xyzCrop(appname,username):
    print "username ",username
    print "appname", appname
    pathFix = setpath()
    f = '%s/%s/static/%s/abcCrop.jpg'%(pathFix,appname,username)
    vision = VisionApi()
    #	image_file = Image.open(f) # open colour image
    #        image_file = image_file.convert('1') # convert image to black and white
    #        image_file.save(f)

    print("vision api has been instantiated..passsing image file next step..")
    texts = vision.detect_text(f)
    # ("/home/administrator/Documents/AngelFiles/imageTxtExt/images/hem/SCAN_COPY_0002.jpg")
    #	print re.findall(r"Bill Amount After Due Date+.+Due Date applicable for current bill amount only",str(texts))

    # "/home/axdministrator/Documents/AngelFiles/imageTxtExt/images/DKYC/jpg/prefix-7.png") #/home/administrator/Documents/AngelFiles/imageTxtExt/images/ekyc/prefix-07.png")
    imagetext = []
    extText = []
    try:
        for filename, text in texts.items():
            k = extract_descriptions(filename, text)
            extText.append(k)
            print("extText : ",extText)
            imagetext.append(text[0][u'description'])

            # soup = BeautifulSoup(texts)
            # print soup
            #	 f=open("/home/administrator/Documents/AngelFiles/payInOutAutomation/dumpofimagetext.txt",'w')
            #	 f.write(texts)
        k = ' '.join(imagetext)
        idx = k.find(str(400069))#360006,400069
        # print idx

        # subs = s[:idx+1]
        # print subs
        k = k[idx - 120:idx + 6]
        imagetext1 = []
        print (imagetext[0].split('\n'))[2],(imagetext[0].split('\n'))[3]
        print(imagetext[0].split('\n'))
        imagetext1 = []
        for i in imagetext[0].split('\n'):
            imagetext1.append(i.lower())
        # nameMatch = difflib.get_close_matches('RATANBEN VALJIBHAI BALASARA'.lower(),imagetext1)
        # pattern = 0.0
        # count = 0
        # if len(nameMatch) == 0:
        #     for ij in imagetext1:
        #         pattern = difflib.SequenceMatcher(None,'RATANBEN VALJIBHAI BALASARA'.lower(),ij).ratio()
        #         print pattern
        #         count += 1
        #         if count == 5:
        #             break
        # print(nameMatch)
        print(imagetext1)
        accountno = []
        acifsc = []
        '''for i in imagetext1:
            print i
            p = re.findall(r'[0-9]{8,20}',i.replace(' ',''))
            print 'p',p
            if len(p) > 0:
                accountno.append(p)

            q = re.findall(r'[a-z]{2,4}[0-9]{7,11}', i.replace(' ',''))
            print 'q',q
            if len(q) > 0:
                acifsc.append(q)
        print "---",accountno[0]
        print "---",acifsc[0]'''

        print("k : ",k)
        return imagetext
    except:
        pass

# p = re.findall(r'(IN[A-Z]{1}[0-9]{2,3}[A-Z0-9]{5,6})',imagetext.replace(' ',''))

def mutualequityData(appname,username,imgid,cp):
    print "username ",username
    print "appname", appname
    print "crop imgid", imgid
    print "crop value", cp
    pathFix = setpath()
    f = '%s/%s/static/%s/abcCrop%s.jpg'%(pathFix,appname,username,imgid)
    nfil = '%s/%s/static/%s/'%(pathFix,appname,username)
    os.system("convert  "+f+" -colorspace Gray  -unsharp 80x20+.70+0 resize 1024X768 "+nfil+"tempC.jpg")
    f = '%s/%s/static/%s/tempC.jpg'%(pathFix,appname)
    vision = VisionApi()
    #	image_file = Image.open(f) # open colour image
    #        image_file = image_file.convert('1') # convert image to black and white
    #        image_file.save(f)

    print("vision api has been instantiated..passsing image file next step..")
    texts = vision.detect_text(f)
    # ("/home/administrator/Documents/AngelFiles/imageTxtExt/images/hem/SCAN_COPY_0002.jpg")
    #	print re.findall(r"Bill Amount After Due Date+.+Due Date applicable for current bill amount only",str(texts))

    # "/home/axdministrator/Documents/AngelFiles/imageTxtExt/images/DKYC/jpg/prefix-7.png") #/home/administrator/Documents/AngelFiles/imageTxtExt/images/ekyc/prefix-07.png")
    imagetext = []
    extText = []
    try:
        for filename, text in texts.items():
            k = extract_descriptions(filename, text)
            extText.append(k)
            #print("extText : ",extText)
            imagetext.append(text[0][u'description'])

        k = ' '.join(imagetext)
        print "Hi K ",k.title()
        p = imagetext
        print "p", p[0].split("\n")[0:-1]
        # ISIN TEXT re.findall(r'(IN[A-Z]{1}[0-9]{2,3}[A-Z0-9]{5,6})',imagetext[0].replace(' ',''))
        # FOLIO NO re.findall(r'([0-9]{8,15})',imagetext[0].replace(' ',''))
        data = []
        if cp == "23" or cp == "29" or cp == "35": #ISIN NO
            imagetext[0] = ''.join(re.findall(r'[a-zA-Z0-9]',imagetext[0]))#.replace(".", '')
            data = re.findall(r'(IN[A-Z]{1}[0-9]{2,3}[A-Z0-9]{5,6})',imagetext[0].replace(" ",''))
            print "isin data",data
            return data
        elif cp == "31":    #folio no
            data = re.findall(r'([0-9]{8,15})',imagetext[0].replace(' ',''))
            print "folio no", data
            return data
        elif cp == "22": #uploded date
            data = re.findall(r'([0-9]{1,2}[-]{0,1}[A-Za-z]{2,3}[-]{0,1}[0-9]{2,4})', imagetext[0].replace(' ', ''))
            print data
            return data
        elif cp == "21" or cp == "33": # DP ID
            data = re.findall(r'([A-Za-z]{0,2}[0-9]{3,9})', imagetext[0].replace(' ', ''))
            print data
            return data
        else:
            return p[0].split("\n")[0:-1]
    except:
        pass


def xyzACCrop(appname,username,imgid):
    print "username ",username
    print "appname", appname
    print "crop imgid", imgid
    pathFix = setpath()
    f = '%s/%s/static/%s/abcCrop%s.jpg'%(pathFix,appname,username,imgid)
    nfil = '%s/%s/static/%s/'%(pathFix,appname,username)
    os.system("convert  "+f+" -colorspace Gray  -unsharp 80x20+.70+0 resize 1024X768 "+nfil+"tempC.jpg")
    f = '%s/%s/static/%s/tempC.jpg'%(pathFix,appname,username)
    vision = VisionApi()
    #	image_file = Image.open(f) # open colour image
    #        image_file = image_file.convert('1') # convert image to black and white
    #        image_file.save(f)

    print("vision api has been instantiated..passsing image file next step..")
    texts = vision.detect_text(f)
    # ("/home/administrator/Documents/AngelFiles/imageTxtExt/images/hem/SCAN_COPY_0002.jpg")
    #	print re.findall(r"Bill Amount After Due Date+.+Due Date applicable for current bill amount only",str(texts))

    # "/home/axdministrator/Documents/AngelFiles/imageTxtExt/images/DKYC/jpg/prefix-7.png") #/home/administrator/Documents/AngelFiles/imageTxtExt/images/ekyc/prefix-07.png")
    imagetext = []
    extText = []
    try:
        for filename, text in texts.items():
            k = extract_descriptions(filename, text)
            extText.append(k)
            print("extText : ",extText)
            imagetext.append(text[0][u'description'])
            # print(text)
            # print(text)
            # print texts
            # print(texts)
            # soup = BeautifulSoup(texts)
            # print soup
            #	 f=open("/home/administrator/Documents/AngelFiles/payInOutAutomation/dumpofimagetext.txt",'w')
            #	 f.write(texts)
        k = ' '.join(imagetext)
        print "Hi K ",k.title()
        print "image text",imagetext[0]
        citytest = GeoText(k.title())
        # cityFinal = (''.join(citytest.cities)).upper()
        cityFinal = ''
        if len(citytest.cities) > 0:
            cityFinal = (citytest.cities[0]).upper()
        print 'city Find----------',cityFinal

        st1 = (stateResult(k)).upper()

        print "state find---",st1

        imagetext1 = []
        for i in imagetext[0].split('\n'):
            imagetext1.append(i.replace(" ",""))
            print 'i',i

        print imagetext1
        data = []
        zipcode = ''
        for i in imagetext1:
            print i
            flag = 0
            p = re.findall(r'[0-9]{5,6}',i.replace(' ',''))
            print 'p', p
            if len(p) > 0:
                zipcode = p
                break
        # accountno = []
        # acifsc = []
        # for i in imagetext1:
        #     print i
        #     flag = 0
        #     p = re.findall(r'[0-9]{8,20}',i.replace(' ',''))
        #     print 'p', p
        #     if len(p) > 0:
        #         accountno.append(p)
        #         flag = 1
        #     if flag == 0:
        #         q = re.findall(r'[a-zA-Z]{2,4}[0-9]{7,8}', i.replace(' ',''))
        #         print 'q',q
        #         if len(q) > 0:
        #             acifsc.append(q)
        #     else:
        #         continue
        # #print "---A/c NO",accountno[0]
        # #print "---Ifsc Code",acifsc[0]
        # data = []
        # if len(accountno) > 0:
        #     data.append(''.join(accountno[0]))
        #     print "---A/c NO", accountno[0]
        # else:
        #     print 'not Found Ac no'
        #     data.append(cityFinal)
        #
        # if len(acifsc) > 0:
        #     data.append(''.join(acifsc[0]))
        #     print "---Ifsc Code", acifsc[0]
        # else:
        #     data.append(st1)
        #print("k : ",k)
        #data = accountno[0]
        data.append(cityFinal)
        data.append(st1)
        data.append(imagetext1)
        data.append(zipcode)
        print 'data',data
        return data
    except:
        pass



def xyzACHolder(appname,username):
    print "username ",username
    print "appname", appname
    pathFix = setpath()	
    f = '%s/%s/static/%s/abcCrop.jpg'%(pathFix,appname,username)
    vision = VisionApi()
    #	image_file = Image.open(f) # open colour image
    #        image_file = image_file.convert('1') # convert image to black and white
    #        image_file.save(f)

    print("vision api has been instantiated..passsing image file next step..")
    texts = vision.detect_text(f)
    # ("/home/administrator/Documents/AngelFiles/imageTxtExt/images/hem/SCAN_COPY_0002.jpg")
    #	print re.findall(r"Bill Amount After Due Date+.+Due Date applicable for current bill amount only",str(texts))

    # "/home/axdministrator/Documents/AngelFiles/imageTxtExt/images/DKYC/jpg/prefix-7.png") #/home/administrator/Documents/AngelFiles/imageTxtExt/images/ekyc/prefix-07.png")
    imagetext = []
    extText = []
    try:
        for filename, text in texts.items():
            k = extract_descriptions(filename, text)
            extText.append(k)
            print("extText : ",extText)
            imagetext.append(text[0][u'description'])
            # print(text)
            # print(text)
            # print texts
            # print(texts)
            # soup = BeautifulSoup(texts)
            # print soup
            #	 f=open("/home/administrator/Documents/AngelFiles/payInOutAutomation/dumpofimagetext.txt",'w')
            #	 f.write(texts)
        k = ' '.join(imagetext)
        print "Hi K ",k
        print "image text",imagetext

        imagetext1 = []
        for i in imagetext[0].split('\n'):
            imagetext1.append(i)
            print 'i',i

        print imagetext1
        accountno = []
        acifsc = []
        for i in imagetext1:
            print i
            flag = 0
            p = re.findall(r'[0-9]{8,20}',i.replace(' ',''))
            print 'p', p
            if len(p) > 0:
                accountno.append(p)
                flag = 1
            if flag == 0:
                q = re.findall(r'[a-zA-Z]{2,4}[0-9]{7,8}', i.replace(' ',''))
                print 'q',q
                if len(q) > 0:
                    acifsc.append(q)
            else:
                continue
        #print "---A/c NO",accountno[0]
        #print "---Ifsc Code",acifsc[0]
        data = []
        if len(accountno) > 0:
            data.append(''.join(accountno[0]))
            print "---A/c NO", accountno[0]
        else:
            print 'not Found Ac no'
            data.append('Not Found')

        if len(acifsc) > 0:
            data.append(''.join(acifsc[0]))
            print "---Ifsc Code", acifsc[0]
        else:
            data.append('Not Found IFSc code')
        #print("k : ",k)
        #data = accountno[0]
        data.append(imagetext)
        print 'data',data
        return data
    except:
        pass

