from django.shortcuts import render
from django.forms import formset_factory

from .forms import CampaignSettingsForm

from .utils import *


def index(request):
    template = 'create_campaign/create_banner.html'
    campaigns_formset = formset_factory(CampaignSettingsForm)
    formset = campaigns_formset(request.POST or None)
    if formset.is_valid():
        for form in formset:
            campaign_id = CreateCampaign(
                *form.cleaned_data.values()
            ).create_campaign()
            # ad_group_id = CreateAdGroup(
            #     campaign_id,
            #     0
            # ).create_ad_group()
            # creatives = (
            #     CreateHtmlCreatives(
            #         ad_group_id,
            #         'Dis18-soap'
            #     )
            # )
            # creatives.get_creatives()
            # creatives.create_creatives()
    context = {'formset': formset}
    return render(request, template, context)

