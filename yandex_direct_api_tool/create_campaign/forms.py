from django import forms


class FormsCount(forms.Form):
    count = forms.IntegerField(label='Количество кампаний')


class AdGroupsCount(forms.Form):
    count = forms.IntegerField(label='Количество групп')


class CampaignSettingsForm(forms.Form):
    campaign_name = forms.CharField(label='Название РК')
    cpm = forms.IntegerField(min_value=20, label='Ставка')
    total_budget = forms.IntegerField(min_value=1000, label='Бюджет')
    date_start = forms.CharField(
        label='Дата старта',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    date_end = forms.CharField(
        label='Дата завершения',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    frequency_cap = forms.IntegerField(label='Частота')
    frequency_period = forms.IntegerField(label='Период частоты')
    ad_group_count = forms.IntegerField(label='Количество групп объявлений')


class AdGroupSettingsForm(forms.Form):
    region_choices = [
        (0, 'RF'),
        (1, 'Some Region')
    ]
    ad_group_name = forms.CharField(label='Название', max_length=50)
    region_choice_field = forms.ChoiceField(
        widget=forms.RadioSelect, choices=region_choices
    )


class CreativeSettings(forms.Form):
    first_pixel = forms.CharField(required=False)
    second_pixel = forms.CharField(required=False)
