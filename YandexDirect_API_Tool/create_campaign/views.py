from django.shortcuts import render

from .forms import CampaignSettingsForm

import campaigns_create


def index(request):
    template = 'index.html'
    form = CampaignSettingsForm(request.GET or None)
    if form.is_valid():
        campaigns_create.CreateCampaign(
            form.cleaned_data['campaign_name'],
            60,
            form.cleaned_data['total_budget'],
            '2023-12-01',
            '2023-12-05',
            7,
            30,
        ).create_campaign()
    context = {'form': form}
    return render(request, template, context)

