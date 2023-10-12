from django.shortcuts import render

from .forms import CampaignSettingsForm


def index(request):
    template = 'index.html'
    form = CampaignSettingsForm(request.GET or None)
    context = {'form': form}
    return render(request, template, context)

