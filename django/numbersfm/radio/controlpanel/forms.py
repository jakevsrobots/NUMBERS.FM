from django import forms
from radio.models import Show, StationStatusUpdate


class StationStatusUpdateForm(forms.ModelForm):
    is_live = forms.ChoiceField(choices=(
            (True, 'Live'),
            (False, 'Archive')
            ))
    
    class Meta:
        model = StationStatusUpdate
        exclude = ('timestamp',)

    def clean(self):
        # clear out extra data if it's an archive stream
        if not self.cleaned_data.get('is_live') or self.cleaned_data.get('is_live') == 'False':
            self.cleaned_data['current_show'] = None
            self.cleaned_data['current_song'] = ''
        return self.cleaned_data
