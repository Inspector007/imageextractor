import csv
import pandas as pd
import collections
import itertools
import re
import time
from multiprocessing import Pool
from testdate import mmyydd
import os
import shutil
import glob
from Setpath import setpath
#exchangeF='/home/puneet/Desktop/deepak/deepak/Family31052016/UCC-MCX/data/MCXFinal.csv'
#backOff='/home/puneet/Desktop/deepak/deepak/Family31052016/UCC-MCX/data/mcdx_active.csv'


def analysisData():
	pathFix = setpath()
	if os.path.isdir('%s/mysite/document/output' %(pathFix)) == True:
		shutil.rmtree('%s/mysite/document/output' %(pathFix))
	lstdate = mmyydd()
	fileName1 = ''
	fileName2 = ''	
	for i in glob.glob('%s/mysite/document/ucc/%s/%s/%s/*' %(pathFix,lstdate[1],lstdate[0],lstdate[2])):
		fileName1 = i.split('/')[-1]
		print fileName1
	for i in glob.glob('%s/mysite/document/bo/%s/%s/%s/*' %(pathFix,lstdate[1],lstdate[0],lstdate[2])):
		fileName2 = i.split('/')[-1]
		print fileName2

	exchangeF = '%s/mysite/document/ucc/%s/%s/%s/%s' %(pathFix,lstdate[1],lstdate[0],lstdate[2],fileName1)
	backOff = '%s/mysite/document/bo/%s/%s/%s/%s' %(pathFix,lstdate[1],lstdate[0],lstdate[2],fileName2)


	# di.setdefault(k,[]).append(e)

	t0 = time.asctime()

	print "t0 : ",t0

	#mobile 
	mcount1 = 0
	mc1= "Dummy updated and Back office Blank"
	mcount2 = 0
	mc2 = "Dummy updated and Back offfice other number"
	mcount3 = 0
	mc3 = "Dummy updated and Back offfice has Same number"
	mcount4 = 0
	mc4 = "UCC Blank and Back Office Blank"
	mcount5 = 0
	mc5 = "UCC Blank and Back Office has Other number"
	mcount6 = 0
	mc6 = "UCC Blank and Back Office has Dummy"
	mcount7 = 0
	mc7 = "UCC has Correct number and Back office has Blank"
	mcount8 = 0
	mc8 = "UCC has Correct number and Back office has Dummy"
	mcount9 = 0
	mc9 = "UCC and Back Office has different Number"
	mcount10 = 0
	mc10 = "UCC has Incorrect number  and back office has same"
	mcount11 = 0
	mc11 = "UCC has Incorrect number  and back office has Blank"
	mcount12 = 0
	mc12 = "UCC has Incorrect number  and back office has correct number"

	#Email

	emcount1 = 0
	emc1 = "Dummy updated and Back office Blank"
	emcount2 = 0
	emc2 = "Dummy updated and Back offfice other number"
	emcount3 = 0
	emc3 = "Dummy updated and Back offfice has Same number"
	emcount4 = 0
	emc4 = "UCC Blank and Back Office Blank"
	emcount5 = 0
	emc5 = "UCC Blank and Back Office has Other number"
	emcount6 = 0
	emc6 = "UCC Blank and Back Office has Dummy"
	emcount7 = 0
	emc7 = "UCC has Correct number and Back office has Blank"
	emcount8 = 0
	emc8 = "UCC has Correct number and Back office has Dummy"
	emcount9 = 0
	emc9 = "UCC and Back Office has different Number"
	emcount10 = 0
	emc10 = "UCC And Back Office has blank Numbar and blank Email"



	fdict = {}

	listM = []
	listB = []

	count = 0

	with open (exchangeF,'r') as f1:
		next(f1)
		for i in f1:
			tlist = []
			il = i.split(',')
			#if il[84].strip() == "" or il[84].strip() == "A":
			x  = il[0].strip().lower() #cl_code 0 -- 0
			listM.append(x)
			tlist.append(x)
			x = il[1].strip().lower() #pan -2 -- 3  
			tlist.append(x)
			x = il[3].strip().lower()# 4 Email -- 9
			tlist.append(x)
			x = il[2].strip()# 3 mobile -- 24 
			tlist.append(x)
			#fdict[tlist[0]] = tlist
			count += 1
			if count < 30:
				print tlist
			fdict.setdefault(tlist[0],[]).append(tlist)
	os.mkdir('%s/mysite/document/output/' %(pathFix))

	outf = '%s/mysite/document/output/' %(pathFix)

	#with open(outf+'duplicateWithExchange.csv','w') as f11:
        #	writer=csv.writer(f11, delimiter=',',lineterminator='\n',)
        #	for k,v in fdict.items():
	#        	if len(v) > 1:
	#                	print len(v),'  -  ',v
	#			for vl in v:
	#			#print vl
        #        	        	writer.writerow(vl)


#print  '\n', len(fdict) ,'\n'  

	excClient = [i for i in fdict.iterkeys()]

	fdictBO = {}
	count = 0
	with open (backOff,'r') as f1:
		next(f1)
        	for i in f1:
                	tlist = []
                	il = i.split(',')
                	x = il[0].strip().lower()
			listB.append(x)
                	tlist.append(x)
                	x = il[1].strip().lower()
                	tlist.append(x)
                	x = il[3].strip().lower()
                	tlist.append(x)
               		x = il[2].strip()
                	tlist.append(x)
                	#fdict[tlist[0]] = tlist
			count += 1
			if count < 30:
				print tlist
			fdictBO.setdefault(tlist[0],[]).append(tlist)

	#fdict = {key: value for key, value in fdict.items() if len(value) > 1}

	#print  '\n', len(fdict1) ,'\n'

	#for k,v in fdict.items():
	#	if len(v) > 1:
	#		print len(v),'  -  ',v

	compare2 = lambda x, y: collections.Counter(x) == collections.Counter(y)
	compare3 = lambda x, y, z: collections.Counter(x) == collections.Counter(y) == collections.Counter(z)
	compare4 = lambda a, x, y, z: collections.Counter(a) == collections.Counter(x) == collections.Counter(y) == collections.Counter(z)
	compare5 = lambda a, b, x, y, z: collections.Counter(a) == collections.Counter(b) == collections.Counter(x) == collections.Counter(y) == collections.Counter(z)

	finlst = []
	count_3 = 0
	count_4 = 0
	count_5 = 0
 	count_6 = 0
 	count_7 = 0 

	t1 = time.asctime()
	print "t1: ",t1

	samelst = []
	elselst = []
	for en in excClient:
	#def cusFunc(en):
		tlst = []
		for i in fdict[en]:
			tlst.append(i)
		if en in fdictBO:
			for i in fdictBO[en]:
				tlst.append(i)

		if len(tlst) == 2:
			outp = compare2(tlst[0],tlst[1])
			if outp == False:
				#print tlst
				rtw = tlst
				#print "rtw[0] : ", len(rtw[0]),"rtw[1]: ",len(rtw[1])
				matchFound3 = re.match(r"^([0-9])\1*$", rtw[0][3])
   				matchFound7 = re.match(r"^([0-9])\1*$", rtw[1][3])
			
    				if  matchFound3 != None and rtw[1][3] == "":
        				mcount1 += 1
        				# continue

    				elif matchFound3 != None and rtw[1][3] != rtw[0][3]:
        				mcount2 += 1
        				# print i[0]
        				# continue

	    			elif matchFound3 != None and rtw[1][3] == rtw[0][3]:
        				mcount3 += 1
        				# continue

    				elif rtw[0][3] == "" and rtw[1][3] == "":
        				mcount4 += 1
        				# continue

	    			elif rtw[0][3] == "" and rtw[1][3] != "" and rtw[1][3] != "0" and matchFound7 == None:
        				mcount5 += 1
        				# continue

    				elif rtw[0][3] == "" and matchFound7 != None:
        				mcount6 += 1
	        			# print i[0]
        			# continue

    				elif len(rtw[0][3]) == 10 and rtw[1][3] == "":
        				mcount7 += 1

    				elif len(rtw[0][3]) == 10 and matchFound7 != None:
        				mcount8 += 1

	    			elif len(rtw[0][3]) == 10 and rtw[0][3] != rtw[1][3]:
        				mcount9 += 1

    				elif (len(rtw[0][3]) < 10 or len(rtw[0][3]) > 10) and rtw[0][3] == rtw[1][3]:
        				mcount10 += 1


	    			elif (len(rtw[0][3]) < 10 or len(rtw[0][3]) > 10) and rtw[1][3] == "":
        				mcount11 += 1


    				elif (len(rtw[0][3]) < 10 or len(rtw[0][3]) > 10) and len(rtw[1][3]) == 10:
        				mcount12 += 1
    				else:
        				pass

				if rtw[0][2] == "notprovided@notprovided.com" and rtw[1][2] == "":
        				emcount1 += 1
	
    				elif rtw[0][2] == "notprovided@notprovided.com" and rtw[1][2] != i[0][2]:
        				emcount2 += 1

    				elif rtw[0][2] == "notprovided@notprovided.com" and rtw[1][2] == i[0][2]:
        				emcount3 += 1

	    			elif rtw[0][2] == "" and rtw[1][2] == "":
        				emcount4 += 1

    				elif rtw[0][2] == "" and rtw[1][2] != rtw[0][2]:
        				emcount5 += 1

	    			elif rtw[1][2] == "notprovided@notprovided.com" and rtw[0][2] == "":
        				emcount6 += 1

    				elif rtw[0][2] != "notprovided@notprovided.com"  and rtw[1][2] == "" and rtw[0][2] != "":
        				emcount7 += 1

	    			elif rtw[0][2] != "notprovided@notprovided.com" and rtw[1][2] == "notprovided@notprovided.com" and rtw[0][2] != "":
        				emcount8 += 1

    				elif rtw[0][2] != "notprovided@notprovided.com" and rtw[0][2] != "" and rtw[1][2] == "notprovided@notprovided.com" and rtw[0][2] != rtw[1][2]:
        				emcount9 += 1
				elif rtw[0][3] == "" and rtw[1][3] == "" and rtw[0][2] == "" and rtw[1][2] == "":
					emcount10 +=1
 
				finlst.append(rtw)		
			
			else:
				samelst.append(tlst)


        	elif len(tlst) == 3:
                	outp = compare3(tlst[0],tlst[1],tlst[2])
			count_3 += 1 
			if outp == False:
				#print tlst
				rtw = tlst
				finlst.append(rtw)

	        elif len(tlst) == 4:
			count_4 += 1
        	        outp = compare4(tlst[0],tlst[1],tlst[2],tlst[3])
			if outp == False:        
				#print tlst
				rtw = tlst
				finlst.append(rtw)

	        elif len(tlst) == 5:
			count_5 += 1
        	        outp = compare5(tlst[0],tlst[1],tlst[2],tlst[3],tlst[4])
			if outp == False:
                        	#print tlst
				rtw = tlst
				finlst.append(rtw)
	
		elif len(tlst) > 5:
			count_6 += 1
			print tlst[0][0]
			print '\n\n\n LENGTH IS MORE THAN 5 \n\n\n'
			break
		else:
			elselst.append(tlst)
			count_7 += 1
			#print '--'
			continue

	

	print len(finlst)

	t2 = time.asctime()

	print "t2: ",t2

	#pool = Pool()
	#results =  pool.map(cusFunc,excClient)


	#print finlst

	with open(outf+'mismatchWithExchange.csv','w') as f11:
		writer=csv.writer(f11, delimiter=',')
		for lk in finlst:
			e = list(itertools.chain(*lk))
        		#writer=csv.writer(f11, delimiter=',') #,lineterminator='\n',)
       			#e =''.join(str(lk))
			#e = e.replace("'","")
			#e = e.replace(']','')
			#e = e.replace('[','')
			#e=e.split(',')
			#print e
			writer.writerow(e)


	with open(outf+'duplicateWithExchange.csv','w') as f11:
                writer=csv.writer(f11, delimiter=',')
                for lk in samelst:
                        e = list(itertools.chain(*lk))
                        #writer=csv.writer(f11, delimiter=',') #,lineterminator='$
                        #e =''.join(str(lk))
                        #e = e.replace("'","")
                        #e = e.replace(']','')
                        #e = e.replace('[','')
                        #e=e.split(',')
                        #print e
                        writer.writerow(e)

	'''with open(outf+'elselstWithExchange.csv','w') as f11:
                writer=csv.writer(f11, delimiter=',')
                for lk in elselst:
                        e = list(itertools.chain(*lk))
                        #writer=csv.writer(f11, delimiter=',') #,lineterminator='$
                        #e =''.join(str(lk))
                        #e = e.replace("'","")
                        #e = e.replace(']','')
                        #e = e.replace('[','')
                        #e=e.split(',')
                        #print e
                        writer.writerow(e)'''




	print "count1: ",mcount1,"count2: ",mcount2,"count3: ",mcount3
	print "count4: ",mcount4,"count5: ",mcount5,"count6: ",mcount6
	print "count7: ",mcount7,"count8: ",mcount8,"count9: ",mcount9
	print "count10: ",mcount10,"count11: ",mcount11,"count12: ",mcount12
	print "Final Count : ",(mcount1+mcount2+mcount3+mcount4+mcount5+mcount7+mcount6+mcount8+mcount9+mcount10+mcount11+mcount12)
	#print "RowCount: ",trCount
	print "count1: ",emcount1,"count2: ",emcount2,"count3: ",emcount3
	print "count4: ",emcount4,"count5: ",emcount5,"count6: ",emcount6
	print "count7: ",emcount7,"count8: ",emcount8,"count9: ",emcount9,"count10: ",emcount10
	print "Final Count : ",(emcount1+emcount2+emcount3+emcount4+emcount5+emcount7+emcount6+emcount8+emcount9+emcount10)


	finaloutput = open(outf + "finalCount%s-2.csv" %time.time(), mode="w")

	l = [[mc1,mcount1],[mc2,mcount2],[mc3,mcount3],[mc4,mcount4],[mc5,mcount5],[mc6,mcount6],[mc7,mcount7],
     	[mc8,mcount8],[mc9,mcount9],[mc10,mcount10],[mc11,mcount11],[mc12,mcount12],
     	[emc1,emcount1],[emc2,emcount2],[emc3,emcount3],[emc4,emcount4],[emc5,emcount5],[emc6,emcount6]
     	,[emc7,emcount7],[emc8,emcount8],[emc9,emcount9],[emc10,emcount10]]

	csvwrite = csv.writer(finaloutput, delimiter =",")


	f = len(l)
	#print "f %d" %f
	i = 0
	while i < f:
    		if i == 0:
			csvwrite.writerow([""])
			csvwrite.writerow(["UCC  Moble Reco","Total","Active in Back office","De-active in Back Office"])
        		csvwrite.writerow([""])
    	#print l[i]
    		if i == 12:
			csvwrite.writerow([""])
        		csvwrite.writerow(["UCC  Email Reco","Total","Active in Back office","De-active in Back Office"])
        		csvwrite.writerow([""])
    		csvwrite.writerow(l[i])
    		i += 1


	print "count M ",len(listM),"count B",len(listB)
	print "B - M",len(list(set(listB)-set(listM)))

	tt = []

	tt = list(set(listB)-set(listM))


	finaloutput1 = open(outf + "BackOfficeExtraExchange.csv", mode="w")
	csvwrite1 = csv.writer(finaloutput1, delimiter =",")

	p = 0

	for xyz in tt:
        	xyz1 = []
        	xyz1.append(xyz)
        	#print xyz,xyz1
        	csvwrite1.writerow(xyz1)
	print count_3,"----",count_4,"----",count_5,"----",count_6,"----",count_7
	shutil.rmtree('%s/mysite/document/ucc/' %(pathFix))
	shutil.rmtree('%s/mysite/document/bo/' %(pathFix))




#analysisData()
