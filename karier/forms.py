from django import forms

from .models import TruckModel

"""
class ModelForm(forms.Form):

    status = forms.ChoiceField(label="",
                                initial='',
                                widget=forms.Select(),
                                required=True)

class AccountDetailsForm(forms.Form):
    ...
    adminuser = forms.ModelChoiceField(queryset=User.objects.all())
    def __init__(self, *args, **kwargs):
        accountid = kwargs.pop('accountid', None)
        super(AccountDetailsForm, self).__init__(*args, **kwargs)

        if accountid:
            self.fields['adminuser'].queryset = User.objects.filter(account=accountid)

form = AccountDetailsForm(accountid=3)
"""
class TruckForm(forms.Form):
    TruckModels = forms.ChoiceField(label="Model", choices=(),widget=forms.Select())
    def __init__(self, *args, **kwargs):
        EXTRA_CHOICES = [('ALL', 'ALL'),]
        super(TruckForm, self).__init__(*args, **kwargs)
        choices = [(pt.name, str(pt.name)) for pt in TruckModel.objects.all()]
        choices.extend(EXTRA_CHOICES)
        self.fields['TruckModels'].choices = choices
