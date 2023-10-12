from django import forms


class CampaignSettingsForm(forms.Form):
    campaign_name = forms.CharField()
    # add rest of the settings here later
