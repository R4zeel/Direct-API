from django.shortcuts import render
from django.forms import formset_factory

from .forms import *

from .utils import *

campaigns_list = dict()


def index(request):
    template = 'create_campaign/create_banner.html'
    count_form = FormsCount(request.GET or None)
    campains_quantity = 0
    if count_form.is_valid():
        campains_quantity = count_form.cleaned_data['count']
    formset = (formset_factory(CampaignSettingsForm, extra=campains_quantity))(request.POST or None)
    if formset.is_valid():
        for form in formset:
            campaign_id = CreateCampaign(
                *form.cleaned_data.values()
            ).create_campaign()
            campaigns_list[campaign_id] = form.cleaned_data.ad_groups_count
    context = {
        'formset': formset,
        'count': count_form,
        }
    return render(request, template, context)

def ad_group_create(request):
    template = 'create_campaign/create_ad_group.html'
    formset = (formset_factory(AdGroupSettingsForm, extra=1))(request.POST or None)
    context = {'formset': formset}
    return render(request, template, context)
    
