# import json
# import requests
# import auth_info
#
# LONG_NUMBER = 1000000
#
# TOKEN = auth_info.TOKEN
#
# CLIENT_LOGIN = auth_info.CLIENT_LOGIN
#
# headers = {
#     "Authorization": "Bearer " + TOKEN,
#     "Client-Login": CLIENT_LOGIN,
#     "Accept-Language": "ru",
# }
#
#
# def create_json_object(obj_url, body):
#     json_body = json.dumps(body, ensure_ascii=False).encode('utf8')
#     result = requests.post(obj_url, json_body, headers=headers)
#     return result.json()['result']['AddResults'][0]['Id']
#
#
# class CreateCampaign:
#     def __init__(
#             self,
#             campaign_name: str,
#             cpm: int,
#             budget: int,
#             start_date: str,
#             end_date: str,
#             frequency: int,
#             frequency_period: int,
#     ):
#         self.campaign_name = campaign_name
#         self.cpm = cpm
#         self.budget = budget
#         self.start_date = start_date
#         self.end_date = end_date
#         self.frequency = frequency
#         self.frequency_period = frequency_period
#         self.campaign_id = 0
#
#     def create_campaign(self):
#         campaigns_url = 'https://api.direct.yandex.com/json/v5/campaigns'
#         settings = [
#             {
#                 "Name": self.campaign_name,
#                 "StartDate": self.start_date,
#                 "CpmBannerCampaign": {
#                     "BiddingStrategy": {
#                         "Search": {
#                             "BiddingStrategyType": "SERVING_OFF"
#                         },
#                         "Network": {
#                             "BiddingStrategyType": "CP_MAXIMUM_IMPRESSIONS",
#                             "CpMaximumImpressions": {
#                                 "AverageCpm": self.cpm * LONG_NUMBER,
#                                 "SpendLimit": self.budget * LONG_NUMBER,
#                                 "StartDate": self.start_date,
#                                 "EndDate": self.end_date,
#                                 "AutoContinue": "NO"
#                             },
#                         }
#                     },
#                     "Settings": [
#                         {
#                             "Option": "ADD_METRICA_TAG",
#                             "Value": "NO"
#                         },
#                     ],
#                     "FrequencyCap": {
#                         "Impressions": self.frequency,
#                         "PeriodDays": self.frequency_period
#                     },
#                 }
#             }
#         ]
#         body = {
#             "method": "add",
#             "params": {
#                 "Campaigns": settings,
#             }
#         }
#         self.campaign_id = create_json_object(campaigns_url, body)
#         print(f'Кампания создана. ID - {self.campaign_id}')
#         return self.campaign_id
#
#
# class CreateAdGroup:
#     def __init__(self, campaign_id, region_id):
#         self.campaign_id = campaign_id
#         self.region_id = region_id
#         self.ad_group_id = 0
#
#     def create_ad_group(self):
#         ad_groups_url = 'https://api.direct.yandex.com/json/v5/adgroups'
#         settings = [
#             {
#                 "Name": 'TestInterests',
#                 "CampaignId": self.campaign_id,
#                 "RegionIds": [self.region_id],
#                 "CpmBannerUserProfileAdGroup": dict()
#             }
#         ]
#         body = {
#             "method": "add",
#             "params": {
#                 'AdGroups': settings,
#             }
#         }
#         self.ad_group_id = create_json_object(ad_groups_url, body)
#         print(f'Группа объявлений создана. ID - {self.ad_group_id}')
#         return self.ad_group_id
#
#     def add_targetings(self):
#         body = {
#             "method": "add",
#             "params": {
#                 "AudienceTargets": [
#                     {
#                         "AdGroupId": self.ad_group_id,
#                         "RetargetingListId": (long),
#                         "InterestId": (long),
#                         "ContextBid": (long),
#                         "StrategyPriority": ( "LOW" | "NORMAL" | "HIGH" )
#                     }
#                 ]
#             }
#         }
#         ...
#
#
# class CreateHtmlCreatives:
#     def __init__(self, ad_group_id, creative_name):
#         self.creative_name = creative_name
#         self.ad_group_id = ad_group_id
#         self.creative_id = []
#
#     def get_creatives(self):
#         creatives_url = 'https://api.direct.yandex.com/json/v5/creatives'
#         creatives_body = {
#             "method": "get",
#             "params": {
#                 "SelectionCriteria": {
#                     "Types": ["HTML5_CREATIVE"],
#                 },
#                 "FieldNames": [
#                     'Name',
#                     "Id",
#                     "Width",
#                     "Height"
#                 ],
#             }
#         }
#         json_body = json.dumps(creatives_body, ensure_ascii=False).encode('utf8')
#         result = requests.post(creatives_url, json_body, headers=headers)
#         for creative_info in result.json()['result']['Creatives']:
#             if self.creative_name in creative_info['Name']:
#                 self.creative_id.append(creative_info['Id'])
#
#     def create_creatives(self):
#         ads_url = 'https://api.direct.yandex.com/json/v5/ads'
#         for id in self.creative_id:
#             add_settings = [
#                 {
#                     "AdGroupId": self.ad_group_id,
#                     "CpmBannerAdBuilderAd": {
#                         "Creative": {
#                             "CreativeId": id,
#                         },
#                         "Href": 'https://ya.ru',
#                         'TrackingPixels': {
#                             'Items': [
#                                 'https://wcm.weborama-tech.ru/fcgi-bin/dispatch.fcgi?a.A=im&a.si=9312&a.te=11311&a.he=1&a.wi=1&a.hr=p&a.ra=%25aw_random%25',
#                                 'https://pixel.adlooxtracking.ru/ads/ic.php?_=%25aw_random%25&type=pixel&plat=30&tag_id=238&client=weborama&id1=1081&id2=80&id3=&id4=&id5=11315&id6=0&id7=9312&id11=&id12=russia&id14=$ADLOOX_WEBSITE'
#                             ]
#                         }
#                     },
#                 }
#             ]
#             body = {
#                 "method": "add",
#                 "params": {
#                     'Ads': add_settings
#                 }
#             }
#             ad_id = create_json_object(ads_url, body)
#             print(f'Объявление {ad_id} создано')
#
