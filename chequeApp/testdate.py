from datetime import date

def mmyydd():
	strDate = str(date.today())
	lstDate = strDate[2:].split('-')
	print lstDate[0],lstDate[1],lstDate[2]
	return lstDate


"""
for i in glob.glob('/home/puneet/Desktop/deepak/Projects/mysite/document/bo/%s/%s/%s/*' %(lstDate[1],lstDate[0],lstDate[2])):
    print i
"""
