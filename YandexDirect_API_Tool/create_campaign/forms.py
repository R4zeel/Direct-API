from django import forms


class CampaignSettingsForm(forms.Form):
    campaign_name = forms.CharField(label='Название РК')
    total_budget = forms.IntegerField(min_value=1000, label='Бюджет')
    cpm = forms.IntegerField(min_value=20, label='Ставка')
    date_start = forms.DateField(
        label='Дата старта',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    date_end = forms.DateField(
        label='Дата завершения',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    frequency_cap = forms.IntegerField(label='Частота')
    frequency_period = forms.IntegerField(label='Период частоты')
    # # add rest of the settings here later
