import json
import requests
import auth_info

TOKEN = auth_info.TOKEN

dict_url = 'https://api.direct.yandex.com/json/v5/dictionaries'

headers = {
    "Authorization": "Bearer " + TOKEN,
    "Accept-Language": "ru",
}

body = {
  "method": "get",
  "params": {
    "DictionaryNames": ["FilterSchemas"] 
  }
}
# , "AudienceInterests" , "FilterSchemas"  "GeoRegions", "GeoRegionNames", 
json_body = json.dumps(body, ensure_ascii=False).encode('utf8')
result = requests.post(dict_url, json_body, headers=headers)
print(result.json())

# with open('geo_dict.json', 'w', encoding='utf8') as f:
#     json.dump(result.json(), f, ensure_ascii=False, indent='')

with open('json/filters_dict.json', 'w', encoding='utf8') as f:
    json.dump(result.json(), f, ensure_ascii=False, indent='')