import requests
from dicttoxml import dicttoxml
import xmltodict

data = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><ns3:EPCISDocument schemaVersion="1.2" creationDate="2018-10-08T21:15:07.528Z" xmlns:ns2="urn:epcglobal:cbv:mda" xmlns:ns3="urn:epcglobal:epcis:xsd:1"><EPCISBody><EventList><ObjectEvent><eventTime>2012-10-08T21:15:07.528Z</eventTime><eventTimeZoneOffset>-05:00</eventTimeZoneOffset><baseExtension><eventID>urn:uuid:4da50fe1-f363-47a8-8b82-b9e98ef7e831</eventID></baseExtension><epcList><epc>urn:ibm:ift:product:serial:obj:1550979232140.0081.5157</epc></epcList><action>ADD</action><bizLocation><id>urn:ibm:ift:location:loc:1550979232140.1</id></bizLocation><extension><sourceList><source type="urn:epcglobal:cbv:sdt:owning_party">urn:ibm:ift:location:loc:1550979232140.1</source></sourceList><destinationList><destination type="urn:epcglobal:cbv:sdt:owning_party">urn:ibm:ift:location:loc:1550979232140.1</destination></destinationList></extension></ObjectEvent></EventList></EPCISBody></ns3:EPCISDocument>';

print (xmltodict.parse(data)['EPCISDocument'])

exit();

print("Hey ravi")
dictionary = {
        'EPCISDocument': {"EventList": {"AggregationEvent" : { "eventTime" :"1", "minute":"30","seconds": "40"},
    
        'place': {"street":"40 something", "zip": "00000"}
    }


xml = dicttoxml(dictionary, custom_root='test', attr_type=False)
print(xml)
exit();




headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
  'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
  'apikey': 'Mu-jHAjlMjHHiUJR87TLQ-X3kGKw90FT8kGtL-DlMfab'
}

response = requests.post('https://iam.ng.bluemix.net/oidc/token', headers=headers, data=data)


headers = {
    'Content-Type': 'application/json',
}

data = response.text

response = requests.post('https://fs-identity-proxy.mybluemix.net/exchange_token/v1/organization/78b25879-313e-4f18-9d62-61c9c3e3929b'
	, headers=headers, data=data)

r_json = response.json();

#print(r_json['onboarding_token']);

headers = {
    'Content-Type': 'application/xml',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + r_json["onboarding_token"],
}


# data = open('/Users/Ravi/Documents/Capstone_Project_499/IBM_API/thakur.xml', 'rt')
data = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><ns3:EPCISDocument schemaVersion="1.2" creationDate="2018-10-08T21:15:07.528Z" xmlns:ns2="urn:epcglobal:cbv:mda" xmlns:ns3="urn:epcglobal:epcis:xsd:1"><EPCISBody><EventList><ObjectEvent><eventTime>2012-10-08T21:15:07.528Z</eventTime><eventTimeZoneOffset>-05:00</eventTimeZoneOffset><baseExtension><eventID>urn:uuid:4da50fe1-f363-47a8-8b82-b9e98ef7e831</eventID></baseExtension><epcList><epc>urn:ibm:ift:product:serial:obj:1550979232140.0081.5157</epc></epcList><action>ADD</action><bizLocation><id>urn:ibm:ift:location:loc:1550979232140.1</id></bizLocation><extension><sourceList><source type="urn:epcglobal:cbv:sdt:owning_party">urn:ibm:ift:location:loc:1550979232140.1</source></sourceList><destinationList><destination type="urn:epcglobal:cbv:sdt:owning_party">urn:ibm:ift:location:loc:1550979232140.1</destination></destinationList></extension></ObjectEvent></EventList></EPCISBody></ns3:EPCISDocument>';

response = requests.post('https://fs-connector.mybluemix.net/fs/connector/v1/assets', headers=headers, data=data)

print(response.text)

