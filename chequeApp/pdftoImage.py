import glob
import PythonMagick
import os
#from PIL import Image
#from googleOCR import VisionApi
from pyPdf import PdfFileWriter, PdfFileReader
import time

def splitpdfintoimages(cid,pathFix):
	count = 0
	if os.path.isdir('%s' % (pathFix)) == True:
		if os.path.isdir('%s/pdfFile' % (pathFix)) == False:
			os.mkdir('%s/pdfFile' % (pathFix))
		else:
			os.system('rm  -r %s/pdfFile/*' % (pathFix))
		pdfl = "%s/crack.pdf"%(pathFix)
		if os.path.isdir('%s/imgFile' % (pathFix)) == False:
			os.mkdir('%s/imgFile' % (pathFix))
		else:
			os.system('rm  -r %s/imgFile/*' % (pathFix))
		os.system("convert -density 300 "+pdfl+" %s/imgFile/page_.jpg"% (pathFix))
		for f in glob.glob('%s/imgFile/*' % (pathFix)):
			count += 1

		return count
	else:
		print 'Folder not available.'
		return count

"""        if os.path.isdir('%s/pdfFile' % (pathFix)) == True:
            for f in glob.glob('%s/pdfFile/*' %(pathFix)):
                os.remove(f)
        else:
            os.mkdir('%s/pdfFile' % (pathFix))

        if os.path.isdir('%s/imgFile' % (pathFix)) == True:
            for f in glob.glob('%s/pdfFile/*' %(pathFix)):
                os.remove(f)
        else:
            os.mkdir('%s/imgFile' % (pathFix))
        inputpdf = PdfFileReader(open("%s/crack.pdf" %(pathFix), "rb"))

        print "enter",time.ctime()
        for i in xrange(inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open("%s/pdfFile/%s.pdf" % (pathFix,i), "wb") as outputStream:
                output.write(outputStream)
        print "exit",time.ctime()
        count = 0
        pdfList = []
        path = str(pathFix)
        for f in glob.glob('%s/pdfFile/*' %(pathFix)):
            img = PythonMagick.Image()
            img.density("300")
            print f
            pathX= str(f)
            img.read(pathX) # read in at 300 dpi
            path11 = str("%s/imgFile/%d.jpg" %(pathFix, count))
            img.write(path11)
            print count,"\n",f
            count += 1
            pdfList.append("%s/imgFile/%d.jpg" %(pathFix, count))

        print len(pdfList)

        for f in pdfList:
            print f

        return pdfList
"""
#for f in glob.glob('/home/puneet/Desktop/deepak/pdfFile/*'):
#	os.remove(f)
#import Image
#im = Image.open("abc.jpg")
#im.save("abc.jpg")