import requests

url = "http://www.insecam.org/en/jsoncountries/"

resp = requests.get(url)

data = resp.json()
countries = data['countries']

for key, value in countries.items():
    print(f'Code: ({key}) - {value["country"]} / ({value["count"]}) ')
    print("")

try:
    country = input("Code(##) : ")

res = requests.get(
    f"http://www.insecam.org/en/bycountry/{country}"
)
last_page = re.findall(r'pagenavigator\("?page=", (\d+)', res.text)[0]

for page in range(int(last_page)):
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}/?page={page}
)
	find_ip = re.findall(r"http://\d+. \d+.\d+.\d+:\d+", res.text)
	with open(f'{country}.txt',  'w') as f:
	for ip in find_ip:
	print("")
	print(ip)
	f.write(f'{ip}\n')
	except:
	pass
	finnaly:
	exit()