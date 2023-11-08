import json
import requests
import yandex_direct_api_tool.auth_info as auth_info

TOKEN = auth_info.TOKEN

CLIENT_LOGIN = auth_info.CLIENT_LOGIN

dict_url = 'https://api.direct.yandex.com/json/v5/dictionaries'

headers = {
    "Authorization": "Bearer " + TOKEN,
    "Client-Login": CLIENT_LOGIN,
    "Accept-Language": "ru",
}

body = {
    "method": "get",
    "params": {
        "DictionaryNames": ["AudienceDemographicProfiles"]
        # 'SelectionCriteria': {
        #     'CampaignIds': [98579490]
        # },
        # 'FieldNames': ['Name', 'RegionIds']
    }
}
# , "AudienceInterests" , "FilterSchemas"  "GeoRegions", "GeoRegionNames", 
json_body = json.dumps(body, ensure_ascii=False).encode('utf8')
result = requests.post(dict_url, json_body, headers=headers)
print(result.json())

# with open('geo_dict.json', 'w', encoding='utf8') as f:
#     json.dump(result.json(), f, ensure_ascii=False, indent='')

with open('json/interests.json', 'w', encoding='utf8') as f:
    json.dump(result.json(), f, ensure_ascii=False, indent='')
