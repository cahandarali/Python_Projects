import requests 

start_time = input('Baslangic vaxtini daxil edin: ')
end_time = input('Bitme vaxtini daxil edin: ')
lati_tude = input('Uzunluqu daxil edin: ')
longi_tude = input('Eni daxil edin: ')
max_radiuskm = input('Maksimum radiusu daxil edin: ')
minimum_mag = input('Minimum maqnitud daxil edin: ')

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url,headers={'Accept':'application/json'},params={
	'format':'geojson',
	'starttime':start_time,
	'endtime':end_time,
	'latitude':lati_tude,
	'longitude':longi_tude,
	'maxradiuskm':max_radiuskm,
	'minmagnitude':minimum_mag
	})

data = response.json()

earthquake_list = data['features']
count = 0
for earthquake in earthquake_list:
	count+=1
	print(f"{count}. Place: {earthquake['properties']['place']}. Magnitude: {earthquake['properties']['mag']}.")