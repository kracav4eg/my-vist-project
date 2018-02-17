from django import forms

from .models import TruckModel

class TruckForm(forms.Form):
    TruckModels = forms.ChoiceField(label="Model", choices=(),widget=forms.Select())
    def __init__(self, *args, **kwargs):
        EXTRA_CHOICES = [('ALL', 'ALL'),]
        super(TruckForm, self).__init__(*args, **kwargs)
        choices = [(pt.name, str(pt.name)) for pt in TruckModel.objects.all()]
        choices.extend(EXTRA_CHOICES)
        self.fields['TruckModels'].choices = choices
