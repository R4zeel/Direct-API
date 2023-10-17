import json
import requests
import auth_info

LONG_NUMBER = 1000000

TOKEN = auth_info.TOKEN

CLIENT_LOGIN = auth_info.CLIENT_LOGIN

headers = {
    "Authorization": "Bearer " + TOKEN,
    "Client-Login": CLIENT_LOGIN,
    "Accept-Language": "ru",
}


class CreateCampaign:
    def __init__(
            self,
            campaign_name: str,
            cpm: int,
            budget: int,
            start_date: str,
            end_date: str,
            frequency: int,
            frequency_period: int,
    ):
        self.campaign_name = campaign_name
        self.cpm = cpm
        self.budget = budget
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency
        self.frequency_period = frequency_period
        self.campaign_id = 0

    def create_campaign(self):
        campaigns_url = 'https://api.direct.yandex.com/json/v5/campaigns'
        settings = [
            {
                "Name": self.campaign_name,
                "StartDate": self.start_date,
                "CpmBannerCampaign": {
                    "BiddingStrategy": {
                        "Search": {
                            "BiddingStrategyType": "SERVING_OFF"
                        },
                        "Network": {
                            "BiddingStrategyType": "CP_MAXIMUM_IMPRESSIONS",
                            "CpMaximumImpressions": {
                                "AverageCpm": self.cpm * LONG_NUMBER,
                                "SpendLimit": self.budget * LONG_NUMBER,
                                "StartDate": self.start_date,
                                "EndDate": self.end_date,
                                "AutoContinue": "NO"
                            },
                        }
                    },
                    "Settings": [
                        {
                            "Option": "ADD_METRICA_TAG",
                            "Value": "NO"
                        },
                    ],
                    "FrequencyCap": {
                        "Impressions": self.frequency,
                        "PeriodDays": self.frequency_period
                    },
                }
            }
        ]
        body = {
            "method": "add",
            "params": {
                "Campaigns": settings,
            }
        }

        json_body = json.dumps(body, ensure_ascii=False).encode('utf8')
        result = requests.post(campaigns_url, json_body, headers=headers)
        print(result.json())
        self.campaign_id = result.json()['result']['AddResults'][0]['Id']


class CreateAdGroup:
    def __init__(self, region_id):
        self.region_id = region_id
        self.ad_group_id = 0

    def create_ad_group(self):
        ad_groups_url = 'https://api.direct.yandex.com/json/v5/adgroups'
        settings = [
            {
                "Name": 'TestInterests',
                "CampaignId": 98747112,
                "RegionIds": [self.region_id],
                "CpmBannerUserProfileAdGroup": dict()
            }
        ]
        body = {
            "method": "add",
            "params": {
                'AdGroups': settings,
            }
        }
        json_body = json.dumps(body, ensure_ascii=False).encode('utf8')
        result = requests.post(ad_groups_url, json_body, headers=headers)
        print(result.json())
        self.ad_group_id = result.json()['result']['AddResults'][0]['Id']


def add_targetings():
    ad_targ_url = 'https://api.direct.yandex.com/json/v5/audiencetargets'
    body = {
        "method": "add",
        "params": {
            "AudienceTargets": [
                {
                    "AdGroupId": 5293289501,
                    "InterestId": 50,
                }
            ]
        }
    }
    json_body = json.dumps(body, ensure_ascii=False).encode('utf8')
    result = requests.post(ad_targ_url, json_body, headers=headers)
    print(result.json())


add_targetings()

# def add_video():
#     {
#         "method": "add",
#         "params": { / * required * /
#                   "AdVideos": [{ / * AdVideoAddItem * /
#                                "Url": (string),
#     "VideoData": (base64Binary),
#     "Name": (string)
#     }, ..]
#     }
#     }
#     ...
#
# def create_video_creative():
#     "params" : { /* required */
#         "Creatives" : [{ /* required */
#             "VideoExtensionCreative" : { /* required */
#                 "VideoId" : (string) /* required */
#             }
#         }, ... ]
#     }
#     ...
#
# def create_video_ad():
#     "CpmVideoAdBuilderAd": { / * CpmVideoAdBuilderAdAdd * /
#                            "Creative": { / * AdBuilderAdAddItem * /
#                                        "CreativeId": (long) / * required * /
#     }, / *required * /
#           "Href": (string),
#     "TrackingPixels": { / * ArrayOfString * /
#                       "Items": [(string), ...] / * required * /
#     },
#     "TurboPageId": (long)
#     },
#     ...
#
# adgroupvariants = [CpmBannerKeywordsAdGroupAdd, CpmVideoAdGroupAdd]
