import requests

r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')

r_text = r.text
print(r_text)

r_json = r.json()
print(r_json)
