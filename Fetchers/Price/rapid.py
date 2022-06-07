import requests

url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"1y"}

headers = {
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com",
	"X-RapidAPI-Key": "18aaa5f225mshd2fd2c15294c380p1c254ajsn96439fe174f5"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
