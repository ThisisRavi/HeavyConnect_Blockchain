import requests

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
  'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
  'apikey': 'Mu-jHAjlMjHHiUJR87TLQ-X3kGKw90FT8kGtL-DlMfab'
}

response = requests.post('https://iam.ng.bluemix.net/oidc/token', headers=headers, data=data)

print(response)