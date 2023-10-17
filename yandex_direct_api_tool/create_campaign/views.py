from django.shortcuts import render
from django.forms import formset_factory

from .forms import CampaignSettingsForm, FormsCount

from .utils import *


def index(request):
    count_form = FormsCount(request.GET)
    template = 'create_campaign/create_banner.html'
    extra_c = 0
    if count_form.is_valid():
        extra_c = count_form.cleaned_data['count']
    campaigns_formset = formset_factory(CampaignSettingsForm, extra=extra_c)
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
    context = {'formset': formset,
               'count': count_form}
    return render(request, template, context)

