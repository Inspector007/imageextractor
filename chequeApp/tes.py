


states = ['Arunachal Pradesh','Andhra Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim ','Tamilnadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal','Andaman and Nicobar Islands','Chandigarh','Dadra and Nagar Haveli','National Capital Territory of Delhi','Delhi','Daman and Diu','Lakshadweep','Puducherry']

txt = """ASHIKA STOCK BROKING LIMITED
DPOF Central Depository Services Ltd
TRINITY, 7TH FLOOR.,2261, AUC BOSE ROAD
KOLKATA WEST BENGAL-700020
ASHIKA
Phone 033-22839952 Fax033-22891555
hwinikumargashikagrou
m,dpse
DP Id 12034500
Alc Status Act
Dt 23 MAR
Alc Category Regular Freere Status
Nationality INDIA Stmtcycle Endof Month
Occupation BUSINESS Closure hnit By
SMS Mobile No 9757424653 TUID
RBI Ref No
BSDA Flag
No1 RGESS Fla
Pledge SI Flag No Email DML Flag Yes
First Holder Name
Mr GALAGIRRISH
First Holder PAN AAEPG39l
Birth 06 JUN 1964
Second Holder Name
Second Holder PAN
Dat
Third Holder Name
Third Holder PAN
Birth
Correspond
A WING, FLAT NO 402 4TH FLOOR
Permanent A WING FLAT NO
4TH FLOOR
UMA SHREE CHS LTD. SANE GURUTI
Addres
Addre
UMA SHREECHIS TD SANEGURUI
NAGAR, 50 FEETRDMULUND EAST
NAGAR, 90 FEETRDMULUND EAST
MUMBAL 400081, MAHARASHTRA INDIA
MUMBAI 400081 MAHARASHTRA NDIA
Phone/Fax 9757424653
Phi
757424553
Email
girrishgalagyahoo.
Bank ACType ngs Bank A
CANARA 3ANK-MULUND EAST BRANCH. MUMBAI
Bank
Bank ACN
2674101005397
5HRINATH PLAZA
MICR Code 400015123
LTROAD
IFSC Code CNRB0D025A
MUMBAI 400081, MAHARASHTRA INDIA
CS Flag
Nominees Guardian D
Nominee Details (Name and Address)
FOA Details
Holderl1st2nd 3rd)
POA Reference
POA Master Id POA Name
"""

def stateResult(p):
	st1 = ''
	for s in states:
		s=s.lower()
		if s in p.lower():
			st1 = s
			print st1
			break
	return st1


#hi = stateResult(txt)

#print hi
