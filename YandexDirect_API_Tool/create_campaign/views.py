from django.shortcuts import render
from django.forms import formset_factory

from .forms import CampaignSettingsForm

import campaigns_create


def index(request):
    template = 'index.html'
    campaigns_formset = formset_factory(CampaignSettingsForm, extra=2)
    formset = campaigns_formset(request.GET or None)
    if formset.is_valid():
        for form in formset:
            campaign_id = campaigns_create.CreateCampaign(
                form.cleaned_data['campaign_name'],
                form.cleaned_data['cpm'],
                form.cleaned_data['total_budget'],
                str(form.cleaned_data['date_start']),
                str(form.cleaned_data['date_end']),
                form.cleaned_data['frequency_cap'],
                form.cleaned_data['frequency_period'],
            ).create_campaign()
            ad_group_id = campaigns_create.CreateAdGroup(
                campaign_id,
                0
            ).create_ad_group()
            creatives = (
                campaigns_create.CreateHtmlCreatives(
                    ad_group_id,
                    'Dis18-soap'
                )
            )
            creatives.get_creatives()
            creatives.create_creatives()
    context = {'formset': formset}
    return render(request, template, context)

