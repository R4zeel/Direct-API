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


def create_json_object(obj_url, body):
    json_body = json.dumps(body, ensure_ascii=False).encode('utf8')
    result = requests.post(obj_url, json_body, headers=headers)
    print(result)
    return result.json()['result']['AddResults'][0]['Id']


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
            dump=None
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
        self.campaign_id = create_json_object(campaigns_url, body)
        print(f'Кампания создана. ID - {self.campaign_id}')
        return self.campaign_id


class CreateAdGroup:
    def __init__(self, campaign_id, region_id):
        self.campaign_id = campaign_id
        self.region_id = region_id
        self.ad_group_id = 0

    def create_ad_group(self):
        ad_groups_url = 'https://api.direct.yandex.com/json/v5/adgroups'
        settings = [
            {
                "Name": 'TestInterests',
                "CampaignId": self.campaign_id,
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
        self.ad_group_id = create_json_object(ad_groups_url, body)
        print(f'Группа объявлений создана. ID - {self.ad_group_id}')
        return self.ad_group_id

    def add_targetings(self):
        body = {"method": "add","params": {"AudienceTargets": [{"AdGroupId": self.ad_group_id,"RetargetingListId": (long),"InterestId": (long),"ContextBid": (long),"StrategyPriority": ("LOW" | "NORMAL" | "HIGH")}]}}
        ...


class CreateCreatives:
    def __init__(self, ad_group_id, click_url, banner_name=None, pixel_one=None, pixel_two=None):
        self.banner_name = banner_name
        self.ad_group_id = ad_group_id
        self.creative_id = []
        self.click_url = click_url
        self.pixel_one=pixel_one
        self.pixel_two=pixel_two

    def add_video():
        body = {
            "method": "add",
            "params": {
                "AdVideos": [
                    {
                        "VideoData": None,
                        "Name": str()
                    }
                ]
            }
        }
        ...

    def create_video_creative():
        body = {
            "params" : {
                "Creatives" : [
                    {
                        "VideoExtensionCreative" : {
                            "VideoId" : str()
                        }
                    }
                ]
            }
        }
        ...

    def create_video_ad(self):
        body = {
            "CpmVideoAdBuilderAd": {
                "Creative": {
                    "CreativeId": int()
                },
                "Href": self.click_url,
                "TrackingPixels": {
                    "Items": [
                        self.pixel_one, 
                        self.pixel_two
                    ]
                }
            }
        }
        ...

    def get_banners(self):
        creatives_url = 'https://api.direct.yandex.com/json/v5/creatives'
        creatives_body = {
            "method": "get",
            "params": {
                "SelectionCriteria": {
                    "Types": ["HTML5_CREATIVE"],
                },
                "FieldNames": [
                    'Name',
                    "Id",
                    "Width",
                    "Height"
                ],
            }
        }
        json_body = json.dumps(creatives_body, ensure_ascii=False).encode('utf8')
        result = requests.post(creatives_url, json_body, headers=headers)
        for creative_info in result.json()['result']['Creatives']:
            if self.banner_name in creative_info['Name']:
                self.creative_id.append(creative_info['Id'])

    def create_banners(self):
        ads_url = 'https://api.direct.yandex.com/json/v5/ads'
        for id in self.creative_id:
            add_settings = [
                {
                    "AdGroupId": self.ad_group_id,
                    "CpmBannerAdBuilderAd": {
                        "Creative": {
                            "CreativeId": id,
                        },
                        "Href": self.click_url,
                        'TrackingPixels': {
                            'Items': [
                                self.pixel_one,
                                self.pixel_two
                            ]
                        }
                    },
                }
            ]
            body = {
                "method": "add",
                "params": {
                    'Ads': add_settings
                }
            }
            ad_id = create_json_object(ads_url, body)
            print(f'Объявление {ad_id} создано')

object = CreateCreatives(5308821799)
object.create_creatives()
print(object)

# adgroupvariants = [CpmBannerKeywordsAdGroupAdd, CpmVideoAdGroupAdd]