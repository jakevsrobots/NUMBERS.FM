from django import forms
from radio.models import Show, StationStatusUpdate


class StationStatusUpdateForm(forms.ModelForm):
    
    class Meta:
        model = StationStatusUpdate
        exclude = ('timestamp',)
