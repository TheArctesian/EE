import requests
# import convert
import json
import time

url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"1y"}

headers = {
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com",
	"X-RapidAPI-Key": "18aaa5f225mshd2fd2c15294c380p1c254ajsn96439fe174f5"
}

response = requests.request("GET", url, headers=headers, params=querystring)


# loop through response and change the vaule of timestamp to a human redable format using time 
data = response.json()
for i in range(len(data['data']['history'])):
	data['data']['history'][i]['timestamp'] = time.strftime("%d/%m/%Y", time.localtime(data['data']['history'][i]['timestamp']))

with open('out.json', 'w') as f:
	f.write(json.dumps(data))


