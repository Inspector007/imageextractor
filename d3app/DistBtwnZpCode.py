import urllib2
import json
zipCode1 = "400097+in" # in country code
zipCode2 = "400059+in" # in country code
# key = "AIzaSyCpTcg0pugLpkTTVuI4XigI9B7G9k-0f2o"
# gmapUrlTest = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&key=%s" %(zipCode1,zipCode2,key)
gmapUrl = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&mode=driving&language=en-EN&sensor=false" %(zipCode1,zipCode2)
response = urllib2.urlopen(gmapUrl)
jsongeocode = response.read()
d = json.loads(jsongeocode)
print d['rows'][0]['elements'][0]['distance']['text']

#i = [1,2,3]
#min(i)
