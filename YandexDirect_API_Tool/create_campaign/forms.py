from django import forms


class CampaignSettingsForm(forms.Form):
    campaign_name = forms.CharField(label='Название РК')
    total_budget = forms.IntegerField(min_value=1000, label='Бюджет')
    # add rest of the settings here later
