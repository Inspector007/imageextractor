import MySQLdb

def showClientDetail(id1):
	con = MySQLdb.connect('localhost', 'root', 'root', 'dbTest01')
	print id1
	cursor = con.cursor()
	cursor.execute("select * from dbt1Emp where c_id = '%s'" %(id1))
	clientDetail = cursor.fetchall()
	clientList= []
	for i in clientDetail:
		print i
		for x in i:
			clientList.append(x)

	con.close()
	return clientList

def showmutualClientDetail(id1):
	con = MySQLdb.connect('localhost', 'root', 'root', 'mutual_equity')
	print id1
	cursor = con.cursor()
	cursor.execute("select * from clienttbl where cl_id = '%s'" %(id1))
	clientDetail = cursor.fetchall()
	clientList= []
	for i in clientDetail:
		print i
		for x in i:
			clientList.append(x)

	con.close()
	return clientList


def updateClientDetail(id,acno,ifsc,name):
	con = MySQLdb.connect('localhost', 'root', 'root', 'dbTest01')
	successFlag = 0
	print "hi ",name,acno,ifsc,id
	cursor = con.cursor()
	try:
		cursor.execute("update dbt1Emp set c_name = '%s', c_acno = '%s', c_ifscno = '%s' where c_id = '%s'" %(name,acno,ifsc,id))
		con.commit()
		successFlag = 1
		
	except:
		con.rollback()
	con.close()
	return successFlag



